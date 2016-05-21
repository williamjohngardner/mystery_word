def random_word_generator():

    import random

    with open("words") as opened_file:
        words = opened_file.read().lower().splitlines()

    random_word = random.choice(words).upper()

    return random_word