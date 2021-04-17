import random
import sys
original_number = random.randint(1, 100)
lives, choice, guessed_number = 5, 1, 0


while 1 <= choice <= 3:
    print("")
    print("")
    print("------------------------------")
    print("----------GUESS GAME----------")
    print("------------------------------")
    print("----------1. START------------")
    print("----------2. HELP-------------")
    print("----------3. Exit-------------")
    print("------------------------------")
    choice = int(input("SELECT OPTION : "))
    if choice == 1:
        while lives != 0:
            guessed_number = int(input("Enter Guessed Number : "))
            if guessed_number == original_number:
                print("")
                print("")
                print("------------------------------")
                print("------------------------------")
                print("----------YOU WON-----------")
                print("---Remaining Lives : ", lives, "---")
                print("------------------------------")
                print("------------------------------")
                break

            elif guessed_number < original_number:
                print("")
                print("")
                print("Low Guess. Try a bigger number...")
                lives = lives - 1
            elif guessed_number > original_number:
                print("")
                print("")
                print("High Guess. Try a smaller number...")
                lives = lives - 1
            else:
                lives = lives - 1
        # While loop End
        if lives == 0:
            print("")
            print("")
            print("------------------------------")
            print("----------GAME OVER-----------")
            print("------------------------------")
            print("Out of Lives.......")
            print("------------------------------")
            print("----------GUESS GAME----------")
            print("------------------------------")
    elif choice == 2:
        print("")
        print("")
        print("------------------------------")
        print("-------------HELP-------------")
        print("------------------------------")
        print("Welcome to guess game. Your goal is to guess a number between 1 and 100. You will be given 5 lives. At each failure, 1 life will be lost. At 0 Lifes, Game will end..")
        print("Good Luck")
        print("------------------------------")
        print("-------------HELP-------------")
        print("------------------------------")
    elif choice == 3:
        sys.exit()
