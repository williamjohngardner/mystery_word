import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

random_word = random.choice(words).upper()
print(random_word)

print("Your word contains " + str(len(random_word)) + " letters")

for spaces in random_word:
        print("# ", end='')

random_word_list = list(random_word)

guess = input("\nPlease enter your guess: ").upper()

good_guesses = []
bad_guesses = []

for letter in random_word_list:
    if guess in random_word_list:
        good_guesses.append(guess)
        print("good" + str(good_guesses))
    guess = input("\nPlease enter your guess: ").upper()

    if guess not in random_word_list:
        bad_guesses.append(guess)
        print("bad" + str(bad_guesses))
    guess = input("\nPlease enter your guess: ").upper()
