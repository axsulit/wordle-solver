def load_word_list(filename="5_letter_words.txt"):
    """
    Loads the word list from file.
    """
    with open(filename, "r") as f:
        return [line.strip().lower() for line in f if line.strip()]

def filter_possible_words(word_list, guess, feedback):
    """
    Filters word_list according to the guess and feedback.
    Feedback codes:
      Y - letter is in the correct position.
      W - letter is in the word but in a different position.
      X - letter is not in the word (or extra occurrence beyond Y/W).
    """
    guess = guess.lower()
    required_counts = {} # counts of letters that must be in the word
    letter_has_x = {}

    for i, letter in enumerate(guess): # for each letter in the guess
        code = feedback[i].upper()
        if code in ["Y", "W"]:
            required_counts[letter] = required_counts.get(letter, 0) + 1
        if code == "X":
            # Mark that letter had at least one X.
            letter_has_x[letter] = True

    possible = []
    for word in word_list: 
        valid = True
        
        # check position-specific constraints
        for i, letter in enumerate(guess):
            code = feedback[i].upper()
            if code == "Y":
                # letter must be exactly at this position
                if word[i] != letter:
                    valid = False
                    break
            elif code == "W":
                # letter must appear somewhere in the word, but not at this position
                if word[i] == letter or letter not in word:
                    valid = False
                    break
        if not valid: 
            continue

        # check frequency constraints
        for letter in set(guess):
            count_in_word = word.count(letter)
            required = required_counts.get(letter, 0)
            # if the letter had an X, then the word must have the exact number of occurrences
            if letter in letter_has_x:
                if count_in_word != required:
                    valid = False
                    break
            # if the letter had no X, then the word must have at least the number of occurrences
            else:
                if count_in_word < required:
                    valid = False
                    break
               
        if valid:
            possible.append(word)

    return possible

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

        possible_words = filter_possible_words(possible_words, guess, feedback)
        if not possible_words: # if no possible words, break the loop
            print("No possible words found. Please double-check your inputs.")
            break

        round_number += 1
        
    print(f"\nCongratulations! You've solved the wordle in {round_number} rounds.")