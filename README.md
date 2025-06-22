# AWS Service Name Quiz

A quiz game to guess whether AWS service names start with "Amazon" or "AWS"

## Game Overview

This game tests your knowledge of AWS service names. The service name is displayed without its prefix, and you need to guess whether it starts with "Amazon" or "AWS".

## How to Play

1. Click the "Let's Play" button on the start screen to begin the game.
2. For each service name shown, select either the "Amazon" or "AWS" button.
3. If correct, you'll see a green "Correct!" message.
4. If wrong, you'll see a red "Wrong!" message.
5. The game ends after 3 mistakes or when all questions are answered.
6. On the results screen, you can see your score and click "Play Again" to restart.

## Required Libraries

- Python 3.x
- Pygame

## Installation

```bash
pip install pygame
```

## How to Run

```bash
python main.py
```

## Project Structure

```
game_project/
├── assets/
│   └── images/       # Service icon images
├── data/
│   └── aws_services.py  # AWS service data
├── src/
│   ├── scenes/       # Game scenes
│   │   ├── base_scene.py
│   │   ├── start_scene.py
│   │   ├── game_scene.py
│   │   ├── result_scene.py
│   │   └── main_menu.py
│   └── utils/        # Utilities
│       ├── ui.py
│       └── create_dummy_icons.py
├── main.py           # Main entry point
├── settings.py       # Game settings
└── README.md         # This file
```

## Customization

- Add more AWS services in `data/aws_services.py` to increase the number of quiz questions
- Modify game settings in `settings.py`
- Replace dummy icons with actual AWS service icons in `assets/images/` to improve the visual experience

## Game Features

- Random selection of AWS services for quiz questions
- Score tracking (correct and wrong answers)
- Visual feedback for correct/wrong answers
- Results screen with accuracy percentage and performance evaluation
- Simple and intuitive user interface

Enjoy testing your knowledge of AWS service names!
