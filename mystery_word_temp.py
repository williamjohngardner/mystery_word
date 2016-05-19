import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

random_word = random.choice(words).upper()
random_word_list = list(random_word)
good_guesses = []
bad_guesses = []
turns = 0

print(random_word)
print("Your word contains " + str(len(random_word_list)) + " letters")
for letter in random_word_list:
        print("# ", end='')

guess = input("\nPlease enter your guess: ").upper()

while True:
    for guess in random_word_list:
        if guess not in good_guesses:
            good_guesses.append(guess)
        elif guess not in bad_guesses:
            bad_guesses.append(guess)
        if guess in good_guesses:
            print(str(guess) + ' ', end='')
            # The turn variable should not be incremented here
        else:
            print('_ ', end='')
            turns += 1
print("\n Good Guesses:" + str(good_guesses))
print("\n Bad Guesses: " + str(bad_guesses))
guess = input("\nPlease enter your guess: ").upper()
