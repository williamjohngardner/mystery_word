import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

print("*******MYSTERY WORD GAME*******" +
      "\n*******************************" +
      "\nENTER LETTERS TO GUESS THE WORD")

random_word = random.choice(words).upper()
random_letter_list = list(random_word)
guesses = ''
badguesses = ''
turns = 8

# print(random_word)
print("\n \nYour word contains " + str(len(random_letter_list)) + " letters")
for spaces in random_word:
        print("_ ", end='')

guess = input("\nPlease guess a letter: ").upper()

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
        print("You Win!")
        exit()
    if guess not in random_letter_list:
        badguesses += guess
        turns -= 1
        print("\nYou have", + turns, 'more guesses')
    if turns == 0:
        print("\nYou've used all 8 guesses. Game Over")
        exit()

    print("\n\nLetters Found: " + str(guesses))
    print("\nLetters Missed: " + str(badguesses))
    guess = input("\nPlease guess a letter: ").upper()
