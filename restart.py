def restart_program():

    import sys
    import os

    while True:
        answer = input('Would you like to play again? y or n ')
        if answer == 'y':
            os.execl(sys.executable, 'python', __file__, *sys.argv[1:])
        elif answer == 'n':
            print('Bummer')
            exit()
