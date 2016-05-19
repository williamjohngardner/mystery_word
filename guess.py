word_list = ["E", "X", "I", "T", "E"]
guess = input("Provide input: ").upper()

# print(word_list)

bad_guesses = []

for letter in word_list:
    if guess in word_list:
        print(str(guess) + " ", end='')
        word_list.remove(guess)
        print("good" + str(word_list))

# bad_guesses.append(guess)
# print("bad" + str(bad_guesses))
