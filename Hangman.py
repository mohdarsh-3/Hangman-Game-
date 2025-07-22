import random

# Displaying the Hangman logo at the beginning
print(''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                      
''')

# All stages of the hangman, from full life to no life left
stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# List of possible words for the game
word_list = [
    # Fruits
    "apple", "banana", "mango", "orange", "grape", 
    "papaya", "pineapple", "watermelon", "peach", "cherry",

    # Animals
    "dog", "cat", "horse", "camel", "tiger", 
    "elephant", "monkey", "lion", "giraffe", "zebra",

    # Common Words
    "table", "chair", "house", "light", "clock", 
    "window", "pencil", "bottle", "phone", "paper"
]


# Randomly picking one word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initial lives a player has (6 wrong attempts allowed)
lives = 6

# Display list will show blanks initially, one for each letter
display = ["_"] * word_length

# To keep track of already guessed letters and avoid duplicates
guessed_letters = []

# Flag to control when the game ends
end_of_game = False

# Main game loop
while not end_of_game:
    # Asking the user to input a guess
    user_guess = input("Guess a letter: ").lower()

    # If user has already guessed this letter, warn them and skip
    if user_guess in guessed_letters:
        print(f"You already guessed '{user_guess}'")
        continue

    # Add the guessed letter to the list of guessed letters
    guessed_letters.append(user_guess)

    # If guessed letter is in the word, update the display
    if user_guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == user_guess:
                display[position] = user_guess
    else:
        # If the guess is wrong, reduce a life and show warning
        lives -= 1
        print(f"Wrong guess. You lose a life. {lives} lives left.")

    # Print the current state of the word (with blanks or filled letters)
    print(" ".join(display))

    # Show the corresponding hangman stage based on lives left
    print(stages[6 - lives])

    # Check if the user has won (no blanks left)
    if "_" not in display:
        end_of_game = True
        print("🎉 You Win!")

    # Check if user has lost (no lives left)
    elif lives == 0:
        end_of_game = True
        print(f"💀 You Lose! The word was '{chosen_word}'.")
