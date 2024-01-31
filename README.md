GreedyCat

Overview

The Greedy Cat is a classic arcade game implemented in Python using the Pygame library. The game features a cat(Ginkgo) that the player controls, navigating around the floor plan of an apartment and trying to eat snacks. Each snack eaten makes Ginkgo grows in one cube longer, and if the snack is not eaten by Ginkgo in certain amount of time, Moonpie automatically gets it and her score added by one. The game includes sound effects of wall hitting, and cat happily meowing when getting the snack and of course a scoring system, with the added challenge of a changing difficulty level.

File Structure

│
├── main.py              # Main game loop and game initialization
├── settings.py          # Game settings and constants
├── assets/              # Directory for storing game assets
│   ├── images/          # Icon images like 'greedycat.png'
│   │   └── greedycat.png
│   └── sounds/          # Sound files
│       ├── greedycat_bg.wav
│       ├── greedycat_snack.mp3
│       ├── greedycat_hit.wav
│       └── greedycat_moonpiesnack.mp3
    
├── game/                # Game logic and components
│   ├── cube.py          # Cube class definition
│   ├── cat.py           # Cat class definition
│   └── utilities.py     # Utility functions like 'drawGrid', 'drawWalls', etc.
│
├── ui/                  # UI related module
│   └── display.py       # Functions for score display and window redraw
│
└── README.md            # Project description and instructions


How to Play
Run the main.py script to start the game.
Use the arrow keys to control the cat's direction.

Join me in safeguarding Ginkgo's treats and try to eat as many snacks as possible and prevent colliding with the walls as much as possible.
The game becomes more challenging as Ginkgo's score increases.
