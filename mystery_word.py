import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

random_word = random.choice(words)

print("Your word contains " + str(len(random_word)) + " letters")

guess = input("\nPlease enter your guess: ")