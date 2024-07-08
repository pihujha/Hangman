# Hangman

## Overview
Hangman is a classic word-guessing game. This implementation allows players to guess a word letter by letter, with different modes to either have the computer choose a word, the player set a word, or play a special word.

## How to Play

1. **Starting the Game**:
    - Run the game script.
    - You will be greeted with a welcome message and prompted to select a mode.

2. **Selecting a Mode**:
    - **Mode 1**: The computer will randomly select a word from a predefined list.
    - **Mode 2**: One player will input a word for the other player to guess.
    - **Mode 3**: A special word ("Python") is chosen as the word to guess.

3. **Gameplay**:
    - You will be shown the Hangman scaffold with empty slots representing the letters of the word.
    - Input a single letter guess.
    - If the letter is correct, it will be revealed in the correct positions.
    - If the letter is incorrect, you lose an attempt and part of the hangman figure is drawn.
    - The game continues until you either guess the word correctly or run out of attempts.

4. **Winning and Losing**:
    - Win by guessing all the letters in the word correctly.
    - Lose by running out of attempts before guessing the word. The full hangman figure will be displayed.
    - After each game, you can choose to play again or exit.

## Code Structure

- **`play_again()`**: Prompts the player to play again or exit. If 'Y' is chosen, it restarts the game.
- **`display_word(word, guessed_letters)`**: Displays the current state of the guessed word.
- **`display_hangman(attempts)`**: Shows the hangman figure based on the number of incorrect attempts.
- **`the_game_at_its_core(chosen_word)`**: Core gameplay function that handles letter guessing and game logic.
- **`compvsplayer()`**: Handles the logic for the computer-chosen word mode.
- **`playervsplayer()`**: Handles the logic for the player-chosen word mode.
- **`specialmode()`**: Handles the special mode with a predefined word.
- **`mode_choice(mode)`**: Processes the player's mode selection and starts the corresponding game mode.

## Running the Game

To run the game, ensure you have Python installed on your system. Save the game script to a file (e.g., `hangman.py`), and execute it using the Python interpreter:

```bash
python hangman.py
```

## Credits
This game has been created by Pihu Jha. Enjoy playing!
