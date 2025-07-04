import random

# Word list
word_list = ["apple", "banana", "cherry", "orange", "grapes", "lemon", "brazil", "strawberry", "watermelon", "keyboard", 
             "elephant", "monkey", "library", "vampire", "mystery", "umbrella", "backpack", "dolphin", "robot", "journey"]

# Load all scores from file as a dictionary
def load_scores(filename="score.txt"):
    scores = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.strip().split(":")
                scores[name.strip()] = int(score.strip())
    except FileNotFoundError:
        pass
    return scores

# Save all scores to file
def save_scores(scores, filename="score.txt"):
    with open(filename, "w") as file:
        for name, score in scores.items():
            file.write(f"{name}: {score}\n")

# Show full score table
def show_scoreboard(scores):
    print("\nScoreboard:")
    for name, score in sorted(scores.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {score}")
    print()

# Choose random word
def choose_word(words):
    return random.choice(words)

# Show word with underscores and guessed letters
def display_current_state(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

# Show guessed letters
def display_guessed_letters(guessed_letters):
    return ", ".join(guessed_letters)

# Check for win
def has_won(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

# Main game logic
def play_hangman(word):
    guessed_letters = []
    tries_left = 6

    print("\nWelcome to Hangman!")
    print("You have", tries_left, "tries. Good luck!\n")

    while tries_left > 0:
        print()
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
            return True

    print("\nGame over! You lost. The word was:", word)
    return False

# Ask if player wants to play again
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
    scores = load_scores()
    
    # Ask for player's name
    player = input("Enter your name: ").strip()
    if player == "":
        player = "Player"

    player_score = scores.get(player, 0)
    print(f"\nWelcome, {player}! Your current score is: {player_score}")

    show_scoreboard(scores)

    available_words = word_list.copy()

    while available_words:
        word = choose_word(available_words)
        available_words.remove(word)

        won = play_hangman(word)

        if won:
            scores[player] = scores.get(player, 0) + 1
            print("Your score is now:", scores[player])
            save_scores(scores)

        if not available_words:
            print("\nNo more new words left.")
            break

        if not play_again():
            break

    print("\nThanks for playing! Final score:", scores[player])
    show_scoreboard(scores)

# Run the game
main()