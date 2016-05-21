def user_input():

    import string

    guess = input("\n\nPlease guess a letter: ").upper()

    for item in string.punctuation:
        if guess == item:
            print("\nEntry must be a letter!")
            guess = input("\n\nPlease guess a letter: ").upper()

    if type(guess) == int:
        print("\nEntry must be a letter!")
        guess = input("\n\nPlease guess a letter: ").upper()
    elif len(guess) > 1:
        print("\nPlease enter only one letter at a time!")
        guess = input("\n\nPlease guess a letter: ").upper()
    else:
        return guess
