# dfs-trait-tracker-tft

A DFS algorithm for the game Teamfight Tactics, and specifically for one of the game's augments "Trait Tracker". It takes 2 .json files, one for the unit and their traits associated with them, and the other the number of unique units needed to activate the trait.

I provided the .json files for Set 14's units ranging from 1 to 4 costed units, however I did not define their cost in this case. I will think about adding their cost for future cases where I want to do more. I also provided the trait list for this set, and the minimum requirement for each one to be active. All of this is was done manually.

Feel free to use it yourself, however it could take a few hours to run depending on how large your group size that you are searching for is. There are built-in filters but it is not necessary assuming you have all the data inputted and formatted correctly. It will skip if you do not have enough units to fit the minimum requirement for the trait to be active.

### How to run
1. Use any .json files with the list of units and their traits + list of activatible traits with thresholds. Follow the sample .json files provided for structure.
2. Change group_size value as needed (this is the max amount of people in your team and therefore searches for all resultants in that constraint).
3. If Trait Tracker requires more traits in the future, change relevant values from 8 -> X, where X is the number of traits needed.
4. Run the code (NOTE: This can take anywhere from no time at all, to it taking hours to run in the background of your machine, depends on how large everything is).
