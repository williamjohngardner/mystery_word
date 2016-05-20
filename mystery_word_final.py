import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

random_word = random.choice(words).upper()
random_letter_list = list(random_word)
good_guesses = []
bad_guesses = []
count = 0
guesses = ''
turns = 8
# letter_counter = len(random_word)

print(random_word)
# print(letter_counter)
print("Your word contains " + str(len(random_letter_list)) + " letters")
for spaces in random_word:
        print("_ ", end='')

guess = input("\nPlease enter your guess: ").upper()

while turns > 0:
    guesses += guess
    for char in random_letter_list:
        if char in guesses:
            print(char, end='')
        else:
            print("_ ", end='')
            count += 1
    print(count)
    if count == 0:
        print("You Win!")
        exit()
    if guess not in random_letter_list:
        turns -= 1
        print("You have", + turns, 'more guesses')
    if turns == 0:
        print("You've used all 8 guesses. Game Over")
        exit()
    print("\n Good Guesses:" + str(good_guesses))
    print("\n Bad Guesses: " + str(bad_guesses))
    print(guesses)
    guess = input("\nPlease enter your guess: ").upper()
