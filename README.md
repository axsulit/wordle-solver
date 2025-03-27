# Wordle Solver

Ever felt like Wordle was playing mind games with you? I sure did. Frustrated by endless puzzles and determined not to let online solvers steal all the fun, I built this quirky Python sidekick. It filters through a mountain of 5-letter words to help you pinpoint the possibilities, while you still get to be the mastermind!

## Input

The solver accepts two types of input for each round:

1. **Your Guess**: A 5-letter word
2. **Feedback**: A 5-character string where each character represents:
   - `Y`: Letter is in the correct position
   - `W`: Letter is in the word but in the wrong position
   - `X`: Letter is not in the word

## Output

For each round, the solver will:
- Display the current round number
- Show the number of possible words remaining
- If 50 or fewer words remain, it will list all possible words _(Yes. You still have to work for it!)_
- After each guess, it will filter the word list based on your feedback
- When solved, it will show the number of rounds taken

## Process

1. The solver starts with a comprehensive list of 5-letter words
2. For each round:
   - You enter your guess
   - You provide the feedback from Wordle
   - The solver filters the word list based on:
     - Position-specific constraints (Y and W feedback)
     - Letter frequency constraints (X feedback)
3. The process continues until:
   - You solve the puzzle (YYYYY feedback)
   - You type 'quit'
   - No possible words remain
   - You reach the maximum number of rounds (5)

## Installation

This project uses Rye for dependency management. To get started:

1. Install Rye if you haven't already:
   ```bash
   curl -sSf https://rye.astral.sh/get | bash
   ```

2. Clone this repository and navigate to it:
   ```bash
   git clone https://github.com/axsulit/wordle-solver
   cd wordle-solver
   ```

3. Install dependencies:
   ```bash
   rye sync
   ```

## Usage

Run the solver:
```bash
rye run python main.py
```

Follow the prompts to enter your guesses and feedback. The solver will help you narrow down the possibilities until you find the correct word.

## Word List

The solver includes a comprehensive list of 5-letter words. The word list can be updated using the included scraper:

```bash
rye run python scraper.py
```

This will fetch the latest 5-letter words from bestwordlist.com and save them to `5_letter_words.txt`.