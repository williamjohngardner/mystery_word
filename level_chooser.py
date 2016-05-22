def level_chooser():

    from random_word_generator import random_word_generator
    from random_word_length import random_word_length

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
        random_word_list = list(random_word_generator())
        if level_choice == 1:
            if int(len(random_word_list)) > 6:
                print(len(random_word_list))
                print(random_word_list)
            else:
                return random_word_list
        if level_choice == 2:
            if 11 > int(len(random_word_list)) > 6:
                print(random_word_length())
                print(random_word_list)
            else:
                return random_word_list
        if level_choice == 3:
            if int(len(random_word_list)) < 11:
                print(random_word_length())
                print(random_word_list)
            else:
                return random_word_list
