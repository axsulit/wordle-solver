def load_word_list(filename="5_letter_words.txt"):
    """
    Loads the word list from file.
    """
    with open(filename, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]


if __name__ == "__main__":

    # Load all candidate words from file.
    word_list = load_word_list()
    possible_words = word_list[:]  # start with all words
    round_number = 1

    while round_number <= 5:

        print(f"\nRound {round_number} - {len(possible_words)} possible words remain.")
        
        if len(possible_words) <= 50:
            print("Possible words:", possible_words)
        
        guess = input("Enter your 5-letter guess (or type 'quit' to exit): ").strip().lower()
        if guess == "quit": # exit the game
            break
        if len(guess) != 5 or not guess.isalpha(): # check if the guess is valid
            print("Please enter a valid 5-letter word.")
            continue

        feedback = input("Enter the feedback (Y for right position, W for wrong position, X for not present): ").strip().upper()
        if len(feedback) != 5 or any(ch not in "YWX" for ch in feedback): # check if the feedback is valid
            print("Please enter a valid 5-character feedback (only Y, W, X allowed).")
            continue

        if feedback == "YYYYY":
            break


        round_number += 1
        
    print(f"\nCongratulations! You've solved the wordle in {round_number} rounds.")