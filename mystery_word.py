import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

random_word = random.choice(words)

print("Your word contains " + str(len(random_word)) + " letters")

for letter in random_word:
    print("# ", end='')

guess = input("\nPlease enter your guess: ").upper()

for letter in random_word:
    if guess == letter:
        print("letter found")
    else:
        print("letter not found")
