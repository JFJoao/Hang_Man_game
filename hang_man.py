import random
from replit import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
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
=========''', '''
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

wordlist = ["humanidade","cachorro","espaçonave"]
display = []
end_of_game = False

# choosen_word = random.choice(wordlist).split()
choosen_word = random.choice(wordlist)
# size = len(choosen_word)

word_lenght = len(choosen_word)
lives = 6

for space in range (word_lenght):
  display += "_"

while not end_of_game:

  guess = input("Try a letter of the word.\n").lower()
  clear()

  for position in range (word_lenght):
    letter = choosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in choosen_word:
      lives -= 1
      if lives == 0:
          end_of_game = True
          display = word_lenght
          print("You Lose.")

  print(display)
  if "_" not in display:
    end_of_game = True
    print("You Win!")

  print(stages[lives])
