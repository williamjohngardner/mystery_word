import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

random_word = random.choice(words).upper()
random_word_list = list(random_word)
good_guesses = []
bad_guesses = []
count = 0

print(random_word)
print("Your word contains " + str(len(random_word_list)) + " letters")
for spaces in random_word:
        print("# ", end='')

guess = input("\nPlease enter your guess: ").upper()

while len(bad_guesses) < 8:
    for letter in random_word_list:
        if guess in random_word_list:
            if guess not in good_guesses:
                good_guesses.append(guess)
        else:
            if guess not in bad_guesses:
                bad_guesses.append(guess)
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_ ', end='')
            count += 1
    print("\n Good Guesses:" + str(good_guesses))
    print("\n Bad Guesses: " + str(bad_guesses))
    guess = input("\nPlease enter your guess: ").upper()
else:
    print("Game Over")
