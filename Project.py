import random

# Word list
word_list = ["apple", "banana", "cherry", "orange", "grapes", "lemon"]

# Choose a random word from the list
def choose_word(words):
    return random.choice(words)

# Show the current state of the word with guessed letters and underscores
def display_current_state(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Show guessed letters so far
def display_guessed_letters(guessed_letters):
    return ", ".join(guessed_letters)

# Check if player has guessed all letters in the word
def has_won(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Main game function
def play_hangman():
    word = choose_word(word_list)
    guessed_letters = []
    tries_left = 6

    print("\nWelcome to Hangman!\n")

    while tries_left > 0:
        # Display current word state and guesses
        print("Word:", display_current_state(word, guessed_letters))
        print("Guessed letters:", display_guessed_letters(guessed_letters))
        print("Tries left:", tries_left)

        # Get player's guess
        guess = input("Guess a letter: ").lower()

        # Validate input: single alphabet letter not guessed before
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if guess is correct
        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess.")
            tries_left -= 1

        # Check for win
        if has_won(word, guessed_letters):
            print("\nCongratulations! You won! The word was:", word)
            return  # End current game

    # If out of tries, player loses
    print("\nGame over! You lost. The word was:", word)

# Function to ask if the player wants to play again
def play_again():
    while True:
        answer = input("\nDo you want to play again? (yes/no): ").lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please answer 'yes' or 'no'.")

# Main program loop
def main():
    while True:
        play_hangman()
        if not play_again():
            print("\nThanks for playing Hangman! Goodbye!")
            break

# Start the program
main()
