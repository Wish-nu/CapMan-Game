# CapMan - A Multi-Level Python Game

**CapMan** is a Pac-Man inspired game built in Python using the Pygame library. It features five levels with increasing difficulty, where players guide CapMan to eat food while avoiding ghosts. The game is designed to progressively get harder from Level 3 onward.

## Features:
- Five levels with different layouts and ghost speeds
- Score system: Scores are maintained across levels
- Each level lasts for 10 seconds
- Increasing difficulty, starting very easy and reaching a challenging final level
- "CapMan" title screen on game start

## Key Concepts Used
- **Object-Oriented Programming (OOP)**: Utilized classes to structure the game, allowing for better organization and reusability of code.
- **Game Loop**: Implemented a main game loop that continuously updates the game state and handles user input.
- **Event Handling**: Used Pygame's event handling system to respond to user actions, such as quitting the game or pressing keys.
- **Collision Detection**: Implemented basic collision detection for the player character and game elements, essential for gameplay mechanics.
- **Scoring System**: Designed a scoring mechanism to keep track of player performance across multiple levels.
- **Level Design**: Created different layouts and challenges for each level, enhancing the gameplay experience.
- **Game States**: Managed game states (like start, running, and game over) to control the flow of the game.
- 
## How to Run the Game
1. Ensure you have Python installed on your machine.
2. Install the Pygame library:
   ```bash
   pip install pygame

## Clone the respository to your local machine
git clone https://github.com/Wish-nu/CapMan-Game.git

## Run the capman.py file using Python
python capman.py

## Game Controls
Arrow Keys: Move CapMan (up, down, left, right)

## How the Levels Work:
Level 1: Very easy, slow-moving ghosts
Level 2: Slightly faster ghosts
Level 3: Moderate ghost speed
Level 4: Faster ghosts
Level 5: Fastest speed, the hardest level

## Future Enhancements
Add sound effects for CapMan eating and ghost movements
Save high scores and player names

## License
No license












## Contributing
Contributions are welcome! Feel free to fork this repository and create a pull request with your improvements.

