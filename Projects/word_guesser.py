# WORD GUESSING GAME
# With Hints and Difficulty Levels
import random

# Word Lists
easy_words = [
    "apple",
    "tiger",
    "chair",
    "pizza",
    "water"
]

medium_words = [
    "computer",
    "football",
    "mountain",
    "notebook",
    "elephant"
]

hard_words = [
    "programming",
    "encyclopedia",
    "astronaut",
    "microprocessor",
    "architecture"
]

# Difficulty Selection
print("\n")
print("\tWORD GUESSING GAME")
print("\n")

print("Choose Difficulty Level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

choice = input("\nEnter your choice (1/2/3): ")

# Select Word Based on Difficulty
if choice == "1":
    secret_word = random.choice(easy_words)
    attempts = 8
    level = "Easy"

elif choice == "2":
    secret_word = random.choice(medium_words)
    attempts = 6
    level = "Medium"

elif choice == "3":
    secret_word = random.choice(hard_words)
    attempts = 5
    level = "Hard"

else:
    print("Invalid Choice!")
    exit()

# Variables
guessed_letters = []

# Game Start
print(f"\nDifficulty Level: {level}")
print(f"You have {attempts} attempts.")

# Hint System
print("\nHINTS:")
print(f"• Word Length: {len(secret_word)} letters")
print(f"• First Letter: {secret_word[0]}")

# Main Game Loop
while attempts > 0:

    # Display Current Progress
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check Win Condition
    if "_" not in display_word:
        print("\nCongratulations!")
        print("You guessed the word correctly!")
        break

    # User Input
    guess = input("\nGuess a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Already Guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add Letter
    guessed_letters.append(guess)

    # Correct Guess
    if guess in secret_word:
        print("Correct Guess!")

    # Wrong Guess
    else:
        attempts -= 1
        print("Wrong Guess!")
        print(f"Attempts Left: {attempts}")

# ---------------------------------
# Lose Condition
# ---------------------------------

if attempts == 0:
    print("\nGame Over!")
    print(f"The correct word was: {secret_word}")