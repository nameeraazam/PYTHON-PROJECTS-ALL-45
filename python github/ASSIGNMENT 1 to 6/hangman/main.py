import random

# You can define your word list here instead of importing from a module
word_list = ["apple", "beautiful", "potato"]

# Choose a random word from the list
chosen_word = random.choice(word_list)
print(f"Chosen word: {chosen_word}")  # For debugging, show the chosen word

# Create a list to hold the displayed word, initially with underscores
display = ['_' for _ in range(len(chosen_word))]

# Start the game loop
game_over = False
while not game_over:
    # Ask the player to guess a letter
    guessed_letter = input("Guess a letter: ").lower()  # Convert to lowercase for consistency

    # Check if the guessed letter is in the word
    if guessed_letter in chosen_word:
        print("Match!")
        # Update the display list with the guessed letter in the correct positions
        for index in range(len(chosen_word)):
            if chosen_word[index] == guessed_letter:
                display[index] = guessed_letter
    else:
        print("No match")

    # Show the current state of the word
    print(" ".join(display))

    # Check if the word is completely guessed
    if '_' not in display:
        game_over = True
        print("Congratulations! You've guessed the word.")
