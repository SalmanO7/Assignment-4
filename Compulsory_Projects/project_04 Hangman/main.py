import random

words = ["ALPACIN", "PYTHON", "STREAMLIT", "DEVELOPER", "HANGMAN"]

def new_game():
    return {
        'word': random.choice(words),
        'guessed': [],
        'attempts': 6,
        'wins': 0,
        'losses': 0
    }

def display_status(game):
    display_word = ' '.join([c if c in game['guessed'] else '_' for c in game['word']])
    attempts_visual = '🟢' * game['attempts'] + '🔴' * (6 - game['attempts'])
    print("\n---------------------------")
    print(f"Word: {display_word}")
    print(f"Attempts Left: {attempts_visual}")
    print(f"Guessed Letters: {' '.join(game['guessed'])}")
    print(f"Wins: {game['wins']} | Losses: {game['losses']}")
    print("---------------------------")

def update_game(game, letter):
    letter = letter.upper()
    if letter not in game['guessed']:
        if letter not in game['word']:
            game['attempts'] -= 1
        game['guessed'].append(letter)

    if all(c in game['guessed'] for c in game['word']):
        game['wins'] += 1
        print(f"\n🎉 Congratulations! You guessed the word: {game['word']}")
        return True
    elif game['attempts'] <= 0:
        game['losses'] += 1
        print(f"\n💀 Game Over! The word was: {game['word']}")
        return True
    return False

# --- Main Game Loop ---
game = new_game()

while True:
    display_status(game)
    guess = input("Enter a letter (or type 'new' for new game, 'exit' to quit): ").strip()

    if guess.lower() == 'exit':
        print("Thanks for playing Hangman!")
        break
    elif guess.lower() == 'new':
        game = {
            'word': random.choice(words),
            'guessed': [],
            'attempts': 6,
            'wins': game['wins'],
            'losses': game['losses']
        }
        continue
    elif len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single valid letter.")
        continue

    game_over = update_game(game, guess)
    if game_over:
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again == 'y':
            game = {
                'word': random.choice(words),
                'guessed': [],
                'attempts': 6,
                'wins': game['wins'],
                'losses': game['losses']
            }
        else:
            print("Thanks for playing Hangman!")
            break