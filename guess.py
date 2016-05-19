word_list = ["E", "X", "I", "T"]
guess = input("Provide input: ").upper()

print(word_list)

bad_guesses = []

for letter in word_list:
    if guess in word_list:
        word_list.remove(guess)
        print(word_list)
    else:
        bad_guesses.append(guess)
        print(bad_guesses)

