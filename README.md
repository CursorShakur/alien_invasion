# Alien Invasion

## Overview
Alien Invasion is a base defense and resource management game where players must defend their base from waves of attacking aliens. The game is designed for educational purposes, teaching Python modular programming and game structuring.

## Features
- **Base Defense:** Manage your base's health and defenses against alien attacks.
- **Resource Management:** Earn currency gems by destroying aliens and spend them on upgrades.
- **Enemy Waves:** Face increasingly difficult waves of aliens.
- **Beam Weapon:** Use your beam weapon to destroy aliens before they reach your base.
- **Upgrade System:** Improve your base's defenses to withstand stronger attacks.
- **Story Elements:** Experience a simple narrative that unfolds as you progress.

## Controls
- **Left/Right Arrow Keys:** Move your ship left and right.
- **Spacebar:** Fire your beam weapon.
- **Mouse:** Click on buttons to navigate menus and purchase upgrades.
- **Q:** Quit the game.

## Requirements
- Python 3.x
- Pygame

## Installation
1. Ensure you have Python 3.x installed on your system.
2. Install Pygame by running: `pip install pygame`
3. Clone this repository or download the source code.
4. Navigate to the game directory.
5. Run the game with: `python game.py`

## Docker Installation
1. Ensure you have Docker installed on your system.
2. Build the Docker image: `docker build -t alien-invasion .`
3. Run the game in a container: `docker run -it --rm alien-invasion`

## Game Structure
- **game.py:** Main game loop and initialization.
- **settings.py:** Game configuration settings.
- **player.py:** Player ship mechanics and controls.
- **base.py:** Base defense mechanics.
- **enemies.py:** Enemy wave logic and alien behavior.
- **resources.py:** Resource management system.
- **weapons.py:** Weapon mechanics for the player's beam.
- **story.py:** Narrative elements and text displays.
- **ui.py:** User interface components.
- **utils.py:** Helper functions for various game mechanics.

## Development
This game was developed as an educational project to demonstrate Python modular programming principles. The code is structured to be easily understood and modified.

## Testing
The game includes a testing framework to ensure functionality. Run tests with:
```
python -m unittest discover tests
```

## License
This project is open source and available under the MIT License.

## Credits
Developed as an educational project for learning Python game development. 