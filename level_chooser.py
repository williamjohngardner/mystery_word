def level_chooser():

    from random_word_generator import random_word_generator

    choice = [1, 2, 3]
    level_choice = input("Choose a level: " +
                         "\nEasy:   1" +
                         "\nMedium: 2" +
                         "\nHard:   3" +
                         "\nEnter your choice:")

    if level_choice != choice:
        print("Please only enter a choice between 1 & 3: ")
        level_choice = input("Choose a level: " +
                             "\nEasy:   1" +
                             "\nMedium: 2" +
                             "\nHard:   3" +
                             "\nEnter your choice:")
    else:
        while level_choice == 1:
            if len(random_word_generator()) > 6:
                random_word_generator()
                return random_word_generator()
        while level_choice == 2:
            if len(random_word_generator()) > 6 and len(random_word_generator()) < 11:
                random_word_generator()
                return random_word_generator()
        while level_choice == 3:
            if len(random_word_generator()) < 11:
                random_word_generator()
                return random_word_generator()

