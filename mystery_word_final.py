from random_word_generator import random_word_generator
from user_input import user_input

random_word = random_word_generator()
# import random

# with open("words") as opened_file:
#     words = opened_file.read().lower().splitlines()

print("*******MYSTERY WORD GAME*******" +
      "\n*******************************" +
      "\nENTER LETTERS TO GUESS THE WORD")

# random_word = random.choice(words).upper()
random_letter_list = list(random_word)
guesses = ''
badguesses = ''
goodguesses = ''
turns = 8

# print(random_word)
print("\n \nYour word contains " + str(len(random_letter_list)) + " letters")
for spaces in random_word:
        print("_ ", end='')

# guess = input("\n\nPlease guess a letter: ").upper()
guess = user_input()

while turns > 0:
    if guess in guesses:
        print("\nYou've already guessed that letter.")
    else:
        guesses += guess
    count = 0
    for char in random_letter_list:
        if char in guesses:
            print(char, end='')
        else:
            print("_ ", end='')
            count += 1
    # print(count)
    if count == 0:
        print("\n******************"
              "\n*****You Win!*****"
              "\n******************")
        exit()
    if guess in random_letter_list:
        goodguesses += guess
    if guess not in random_letter_list:
        badguesses += guess
        turns -= 1
    if turns == 0:
        print("\n\n***You've used all 8 guesses. Game Over***")
        print("\nYour word was: " + str(random_word))
        exit()

    print("\n\nLetters Found: " + str(goodguesses))
    print("\nLetters Missed: " + str(badguesses))
    print("\n\nYou have", + turns, 'more guesses')
    # guess = input("\n\nPlease guess a letter: ").upper()
    guess = user_input()