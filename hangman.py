import random

# Waord list
word_list = ["apple", "banana", "cherry", "orange", "grapes", "lemon", "brazil", "strawberry", "watermelon", "keyboard", 
             "elephant", "monkey", "library", "vampire", "mystery", "umbrella", "backpack", "dolphin", "robot", "journey"]

# Load score from file
def load_score(filename="score.txt"):
    try:
        with open(filename, "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 

# Save score to file
def save_score(score, filename="score.txt"):
    with open(filename, "w") as file:
        file.write(str(score))

# Choose a random word
def choose_word(words):
    return random.choice(words)

# Show current word state
def display_current_state(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Show guessed letters
def display_guessed_letters(guessed_letters):
    return ", ".join(guessed_letters)

# Check if player won
def has_won(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Main game function
def play_hangman(word):
    guessed_letters = []
    tries_left = 6

    print("\nWelcome to Hangman!")
    print("You have", tries_left, "tries. Good luck!\n")

    while tries_left > 0:
        print()  # Add blank line
        print("Word:", display_current_state(word, guessed_letters))
        print("Guessed letters:", display_guessed_letters(guessed_letters))
        print("Tries left:", tries_left)

        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
        else:
            print("Wrong guess.")
            tries_left -= 1

        if has_won(word, guessed_letters):
            print("\nCongratulations! You won! The word was:", word)
            return True  # Victory

    print("\nGame over! You lost. The word was:", word)
    return False  # Defeat

# Ask if the player wants to play again
def play_again():
    while True:
        answer = input("\nDo you want to play again? (yes/no): ").lower()
        if answer in ["yes", "y"]:
            return True
        elif answer in ["no", "n"]:
            return False
        else:
            print("Please answer 'yes' or 'no'.")

# Main program
def main():
    available_words = word_list.copy()
    score = load_score()

    print("Current score:", score)

    while available_words:
        word = choose_word(available_words)
        available_words.remove(word)

        won = play_hangman(word)

        if won:
            score += 1
            print("Your score is now:", score)
            save_score(score)

        if not available_words:
            print("\nNo more new words left. Final score:", score)
            break

        if not play_again():
            print("\nThanks for playing! Your final score is:", score)
            break

# Run the game
main()
