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

while True:
    for letter in random_word_list:
        if guess in random_word_list:
            if guess not in good_guesses:
                good_guesses.append(guess)
                for letter in random_word_list:
                    if letter in good_guesses:
                        print(letter, end='')
                    else:
                        print('_', end='')
        else:
            if guess not in bad_guesses:
                bad_guesses.append(guess)
                for letter in random_word_list:
                    if letter in good_guesses:
                        print(letter, end='')
                    else:
                        print('_', end='')

    print("\n Good Guesses:" + str(good_guesses))
    print("\n Bad Guesses: " + str(bad_guesses))
    guess = input("\nPlease enter your guess: ").upper()


