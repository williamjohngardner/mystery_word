def level_chooser():

    from random_word_generator import random_word_generator

    level_choice = int(input("\nChoose a level: " +
                         "\nEasy:   1" +
                         "\nMedium: 2" +
                         "\nHard:   3" +
                         "\nEnter your choice:"))

    if level_choice is not 4 < level_choice > 0:
            print("\nPlease only enter a choice between 1 & 3: ")
            level_choice = int(input("\nChoose a level: " +
                                 "\nEasy:   1" +
                                 "\nMedium: 2" +
                                 "\nHard:   3" +
                                 "\nEnter your choice:"))

    while True:
        random_word = random_word_generator()
        if level_choice == 1:
            if len(random_word) > 6:
                continue
            else:
                break
        if level_choice == 2:
            if len(random_word) > 11 | len(random_word) < 7:
                continue
            else:
                break
        if level_choice == 3:
            if len(random_word) < 11:
                continue
            else:
                break
    else:
        return random_word
