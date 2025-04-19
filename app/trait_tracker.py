from collections import Counter, defaultdict
import json

with open("import/set14_units.json") as f:
    units = json.load(f)
with open("import/set14_traits_threshold.json") as f:
    trait_thresholds = json.load(f)

trait_to_units = defaultdict(list)
for unit in units:
    for trait in unit["Trait"]:
        trait_to_units[trait].append(unit["Name"])

activatable_traits = {trait for trait, ulist in trait_to_units.items() if len(ulist) >= trait_thresholds[trait]}

# if any trait cannot be activated for whatever reason filter them
filtered_units = []
for unit in units:
    filtered_traits = [trait for trait in unit["Trait"] if trait in activatable_traits]
    if filtered_traits:
        filtered_units.append({"Name": unit["Name"], "Traits": filtered_traits})

filtered_units.sort(key=lambda x: len(x["Traits"]), reverse=True)

def compute_potential_active(current_trait_count, remaining_units, trait_thresholds):
    remaining_count = Counter()
    for unit in remaining_units:
        remaining_count.update(unit["Traits"])
    current_active = {trait for trait, count in current_trait_count.items() if count >= trait_thresholds[trait]}
    potential = len(current_active)
    for trait in trait_thresholds:
        if trait in current_active:
            continue
        if current_trait_count[trait] + remaining_count[trait] >= trait_thresholds[trait]:
            potential += 1
    return potential

solutions = []

def dfs(current_group, current_trait_count, group_size=7, start=0):
    if len(current_group) == group_size:
        active = {trait for trait, cnt in current_trait_count.items() if cnt >= trait_thresholds[trait]}
        if len(active) >= 8:
            solutions.append(list(current_group))
        return

    remaining_units = filtered_units[start:]
    potential = compute_potential_active(current_trait_count, remaining_units, trait_thresholds)
    if potential < 8:
        return # prune

    for i in range(start, len(filtered_units)):
        unit = filtered_units[i]
        new_count = current_trait_count.copy()
        for t in unit["Traits"]:
            new_count[t] += 1
        current_group.append(unit)
        dfs(i+1, current_group, new_count, group_size)
        current_group.pop()

group_size = 7  # adjust size if needed
dfs([], Counter(), group_size, 0)

formatted_results = []
for sol in solutions:
    sol_names = [u["Name"] for u in sol]
    sol_trait_count = Counter()
    for u in sol:
        sol_trait_count.update(u["Traits"])
    sol_active = {trait: count for trait, count in sol_trait_count.items() if count >= trait_thresholds[trait]}
    formatted_results.append({
        "unit_names": sol_names,
        "trait_counts": dict(sol_trait_count),
        "active_traits": sol_active,
        "active_count": len(sol_active)
    })

json_filename = f"valid_groups_size_{group_size}.json"

with open(json_filename, "w") as jf:
    json.dump(formatted_results, jf, indent=4)

# for idx, res in enumerate(formatted_results, 1):
#     print(f"Group {idx}:")
#     print("  Units:", ", ".join(res["unit_names"]))
#     print("  Active Traits:", ", ".join(f"{t} ({c})" for t, c in res["active_traits"].items()))
#     print("  Total Active Traits:", res["active_count"])
#     print("-" * 40)
