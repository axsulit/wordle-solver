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

