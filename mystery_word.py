import random

with open("words") as opened_file:
    words = opened_file.read().lower().splitlines()

random_word = random.choice(words).upper()
print(random_word)

print("Your word contains " + str(len(random_word)) + " letters")

def hashtag():
    for spaces in random_word:
        print("# ", end='')
hashtag()

random_word_list = list(random_word)

guess = input("\nPlease enter your guess: ").upper()

good_guesses = []
bad_guesses = []

for letter in guess:
    if letter in good_guesses:
        good_guesses.append(letter)
    else:
        bad_guesses.append(letter)

for letter in random_word_list:
    if guess == letter:
        print("letter found")
        guess = input("\nPlease enter your guess: ").upper()
        continue
    #elif guess != random_word_list[letter]:
    #    print("letter not found")
    #    guess = input("\nPlease enter your guess: ").upper()
    #    continue