import random

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

# Stages of hangman
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

word_list = ["dog", "horse", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
display = ["_"] * word_length
guessed_letters = []

end_of_game = False

while not end_of_game:
    user_guess = input("Guess a letter: ").lower()

    if user_guess in guessed_letters:
        print(f"You already guessed '{user_guess}'")
        continue
    guessed_letters.append(user_guess)

    # Check guessed letter
    if user_guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == user_guess:
                display[position] = user_guess
    else:
        lives -= 1
        print(f"Wrong guess. You lose a life. {lives} lives left.")

    print(" ".join(display))
    print(stages[6 - lives])

    if "_" not in display:
        end_of_game = True
        print("🎉 You Win!")
    elif lives == 0:
        end_of_game = True
        print(f"💀 You Lose! The word was '{chosen_word}'.")
