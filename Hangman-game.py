import random

def get_hangman_stage(incorrect_guesses, max_guesses):
    """Returns the visual stage of the hangman based on incorrect guesses."""
    visual_index = int((incorrect_guesses / max_guesses) * 6) if max_guesses > 0 else 6
    stages = [
        "\n   --------\n   |      |\n   |      \n   |    \n   |      \n   |     \n- - - - -",
        "\n   --------\n   |      |\n   |      O\n   |    \n   |      \n   |     \n- - - - -",
        "\n   --------\n   |      |\n   |      O\n   |      |\n   |      |\n   |     \n- - - - -",
        "\n   --------\n   |      |\n   |      O\n   |     /|\n   |      |\n   |     \n- - - - -",
        "\n   --------\n   |      |\n   |      O\n   |     /|\\\n   |      |\n   |     \n- - - - -",
        "\n   --------\n   |      |\n   |      O\n   |     /|\\\n   |      |\n   |     / \n- - - - -",
        "\n   --------\n   |      |\n   |      O\n   |     /|\\\n   |      |\n   |     / \\\n- - - - -"
    ]
    return stages[visual_index]

def play_hangman():
    """Handles a single full game of Hangman, including setup questions."""
    words = ["BANANA", "COMPUTER", "PYTHON", "PROGRAMMING", "CHALLENGE"]
    word = random.choice(words)
    word_length = len(word)
    
    display = ["_"] * word_length
    incorrect_guesses = 0
    guessed_letters = []

    print("\n==============================")
    print("      Welcome to Hangman!     ")
    print("==============================")

    # Question 1: Ask for player's name
    player_name = input("Enter your name: ").strip()
    if not player_name:
        player_name = "Player"

    # Question 2: Ask for difficulty level
    print(f"\nHello {player_name}! Choose your difficulty level:")
    print("1. Easy (8 Guesses)")
    print("2. Medium (6 Guesses)")
    print("3. Hard (4 Guesses)")
    
    while True:
        choice = input("Enter choice (1, 2, or 3): ").strip()
        if choice == "1":
            max_incorrect_guesses = 8
            break
        elif choice == "2" or choice == "":
            max_incorrect_guesses = 6
            break
        elif choice == "3":
            max_incorrect_guesses = 4
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

    print(f"\nGame started! Good luck, {player_name}!")

    # Main game loop
    while "_" in display and incorrect_guesses < max_incorrect_guesses:
        print(get_hangman_stage(incorrect_guesses, max_incorrect_guesses))
        print("Word to guess:", " ".join(display))
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        print(f"Incorrect guesses remaining: {max_incorrect_guesses - incorrect_guesses}")

        guess = input("Guess a letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("\n❌ Invalid input. Please enter a single letter (A-Z).")
            continue

        if guess in guessed_letters:
            print(f"\n⚠️ You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"\n✅ Correct! '{guess}' is in the word.")
            for i in range(word_length):
                if word[i] == guess:
                    display[i] = guess
        else:
            print(f"\n❌ Sorry, '{guess}' is not in the word.")
            incorrect_guesses += 1

    print(get_hangman_stage(incorrect_guesses, max_incorrect_guesses))
    print("\n--- Game Over ---")
    
    if "_" not in display:
        print(f"🎉 Congratulations {player_name}! You guessed the word: {word}")
    else:
        print(f"💀 Better luck next time, {player_name}. The word was: {word}")

def main():
    """Main loop that handles restarting the script."""
    while True:
        play_hangman()
        
        print("\n--------------------------------")
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing Hangman! Goodbye! 👋")
            break

# CRITICAL: This is what makes the file run when you click play!
if __name__ == "__main__":
    main()
  
