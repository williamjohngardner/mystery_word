import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

random_word = random.choice(words).upper()
random_letter_list = list(random_word)
good_guesses = []
bad_guesses = []
count = 0
letter_counter = len(random_word)

print(random_word)
print(letter_counter)
print("Your word contains " + str(len(random_letter_list)) + " letters")
for spaces in random_word:
        print("# ", end='')

guess = input("\nPlease enter your guess: ").upper()
guesses = ''
guesses += guess

while len(bad_guesses) < 7:
    for letter in random_letter_list:
        if guess in random_letter_list:
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
    print(count)

    if count == 0:
        print("You Win!")
        exit()

    print("\n Good Guesses:" + str(good_guesses))
    print("\n Bad Guesses: " + str(bad_guesses))
    guess = input("\nPlease enter your guess: ").upper()
else:
    print("You've used all 8 guesses. Game Over")

for char in random_letter_list:
    if char in guesses:
        print(char)
    else:
        print("_ ")
        count += 1
