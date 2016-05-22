def restart_program():

    import sys
    import os

    python = sys.executable
    os.execl(python, python, * sys.argv)
if __name__ == "__main__":
    answer = input("\nWould you like to play again? Y or N?")
    if answer.lower().strip() in "y yes".split():
        restart_program()
else:
    exit()
