import random

# List of secret words (fruits)
secret_words = ["apple", "banana", "cherry", "grape", "mango", "orange", "pear", "strawberry"]

def choose_word():
    return random.choice(secret_words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    secret_word = choose_word()
    chances = len(secret_word) + 2
    guessed_letters = []

    print("Welcome to Hangman!")

    while chances > 0:
        print("\nWord:", display_word(secret_word, guessed_letters))
        print("Chances left:", chances)

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            print("Oops! That letter is not in the word.")
            chances -= 1

        if "_" not in display_word(secret_word, guessed_letters):
            print("\nCongratulations! You guessed the word:", secret_word)
            break

    if "_" in display_word(secret_word, guessed_letters):
        print("\nGame over! You ran out of chances. The word was:", secret_word)

if __name__ == "__main__":
    hangman()
