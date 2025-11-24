# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python to practice string manipulation, loops, conditionals, and user input handling. You'll create an interactive console game where players guess letters to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Word Selection and Display

#### Description
Implement the core game setup that randomly selects a word and displays it with hidden letters.

#### Requirements
Completed program should:

- Create a list of at least 10 words for the game to choose from
- Randomly select one word from the list using the `random` module
- Display the word with underscores for each letter (e.g., `_ _ _ _ _` for a 5-letter word)
- Keep track of which letters have been revealed

### 🛠️ User Input and Guess Validation

#### Description
Create a system to accept and validate player guesses, ensuring only valid single letters are processed.

#### Requirements
Completed program should:

- Prompt the player to enter a single letter guess
- Convert input to lowercase for consistency
- Check that the input is a single alphabetical character
- Reject invalid inputs (numbers, symbols, multiple characters) with helpful error messages
- Prevent players from guessing the same letter twice

### 🛠️ Game Logic and State Tracking

#### Description
Implement the core game mechanics that track progress, determine win/loss conditions, and update the game state.

#### Requirements
Completed program should:

- Check if the guessed letter is in the word
- Update the display to reveal correctly guessed letters
- Track the number of incorrect guesses (limit to 6 attempts)
- Maintain and display a list of previously guessed letters
- Detect when the player has won (all letters revealed) or lost (no attempts remaining)
- Display appropriate win or lose messages with the correct word

### 🛠️ (Bonus) Enhanced Features

#### Description
Add extra features to make your Hangman game more engaging and polished.

#### Requirements
Enhanced version could include:

- ASCII art that progressively draws the hangman with each wrong guess
- Multiple difficulty levels with different word lists (easy, medium, hard)
- Option to guess the entire word at once
- Score tracking across multiple rounds
- Category hints for the word (e.g., "Animal", "Food", "Country")
