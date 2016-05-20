import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

random_word = random.choice(words).upper()
random_word_list = list(random_word)
good_guesses = []
bad_guesses = []
count = 0
dash_counter = len(random_word)

print(random_word)
print(dash_counter)
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
    dash_counter -= 1
    print(dash_counter)
    if dash_counter == 0:
        print("You Win!")
        exit()
    print("\n Good Guesses:" + str(good_guesses))
    print("\n Bad Guesses: " + str(bad_guesses))
    guess = input("\nPlease enter your guess: ").upper()
else:
    print("You've used all 8 guesses. Game Over")
