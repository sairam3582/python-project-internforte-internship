# Hangman Game

## Description

The Hangman game is a word-guessing game with origins dating back to Victorian times, as mentioned by Tony Augarde, the author of "The Oxford Guide to Word Games." It's also known as "Birds, Beasts and Fishes" in Alice Bertha Gomme's "Traditional Games" from 1894. In various sources, it's referred to as "Gallows," "The Game of Hangin," or "Hanger."

## Implementation Steps

1. **Select a Secret Word:** The Hangman program randomly selects a secret word from a predefined list of words. This random selection is made possible using Python's random module.

2. **The Game:** A random word, often a fruit name, is chosen from our collection, and the player is given a limited number of chances to guess the word.

3. **Word Guessing:** When a letter in the secret word is guessed correctly, the corresponding letter's position in the word is revealed. The player continues to guess letters until the entire word is revealed or they run out of chances.

4. **Chances:** To make the game more accessible, we've provided players with the word's length plus two additional chances. For instance, if the word to be guessed is "mango," the player receives 5 (the word's length) + 2 = 7 chances to guess the word correctly.

## Features and Learning Objectives

- **Random Word Selection:** The game randomly selects a secret word, adding an element of unpredictability to each playthrough.
- **Word Guessing Challenge:** Players can test their word-guessing skills and vocabulary.
- **Limited Chances:** The game offers a challenging experience by limiting the number of chances available for guessing the word.

## Word List

The Hangman game uses a predefined list of words. You can expand this list with your own words or customize it to suit your preferences. The more diverse the word list, the more exciting the game becomes.

## Instructions

1. Clone this repository to your local machine.
2. Ensure you have Python installed (Python 3 is recommended).
3. Open a terminal or command prompt and navigate to the project directory.
4. Run the Hangman game using the command `python hangman.py`.

Enjoy playing the Hangman game and challenge your word-guessing skills!
