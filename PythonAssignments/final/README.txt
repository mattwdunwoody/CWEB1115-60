IMPORTANT

Get to The Top is a text-based, randomly-generated, top-down, dungeon crawler. You need to fight and loot your way to find the staircase out of each level until you escape the dungeon.

Installation:
1. Requirements
  - Visual Studio 2019
  - Python 3.10+
2. Clone this repository to your machine
3. Open "GetToTheTop.sln" in visual studio 2019
4. Create a new python virtual environment
5. Run

Notes: I'm not sure why, but trying to run this any other way always seems to break the text scrolling and other UI stuff. There are a lot of bugs, and certain things are case-sensitive for some reason. Almost everything is designed to look good in the default terminal window size on a 1080p monitor, so resizing the window or using a different resolution might also break things.

Gameplay:
When you first start the game, you can move, check your inventory, map, or look at the help menu.
The help menu isn't very fleshed-out and it talks about certain combat maneuvers that I don't think I implemented.
Your map is limited to what you can directly see around you, and where you have already been. Unexplored areas are marked with "?" symbols, and walls are marked with "H"s. You are the "@" symbol.
Discovered enemies are marked with a "!" symbol and fallen enemies are marked with a "#". This doesn't always work though for some reason.
Chests are marked with "$" symbols.
You can equip 1 peice of clothing/armor at a time and have an item in each of your hands. Certain items require two-hands though, like longswords/greatswords.
As you progress to higher levels, the loot gets better, but the enemies also get harder. There is no way to recover health, so pick your battles accordingly.
