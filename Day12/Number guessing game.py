

import random
dd = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
          16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30
        , 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
          46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62
        , 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
          79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
def hard():

    print("Total lives", 5)
    flag_va=False
    tt = 5
    k = random.choice(dd)
    while not flag_va:


        b=int(input("enter your number"))
        if b<k:
            print ("too low")
            tt -= 1
            print("you loose one life, Lives left", tt)

            if tt==0:
                print("you loose")
                print("the number was", k)
                flag_va=True
            else:
                print("guess again")
        elif b>k:
            print("too high")
            tt-=1
            print("you loose one life, Lives left",tt)

            if tt==0:
                print("you loose")
                print("the number was", k)

                flag_va=True
            else:
                print("guess again")
        else:
            print("you won")
            break
def easy():
    print("Total lives", 10)
    flag_va = False
    tt = 10
    k = random.choice(dd)
    while not flag_va:

        b = int(input("enter your number"))
        if b < k:
            print("too low")
            tt -= 1
            print("you loose one life, Lives left", tt)
            print("guess again")
            if tt == 0:
                print("you loose")
                print("the number was", k)
                flag_va = True
        elif b > k:
            print("too high")
            tt -= 1
            print("you loose one life, Lives left", tt)
            print("guess again")
            if tt == 0:
                print("you loose")
                print("the number was",k)
                flag_va = True
        elif b == k:
            print("you won")
            break
def number_guessing_project():
    logo = r"""
      / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
     / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
    / /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
    \____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_| 
    """

    print(logo)
    print("Hey welcome to number guessing project")
    print("guess a number bw 1 - 100")
    a = input("please enter dificulty level easy or hard")
    if a == "easy":
        easy()
    elif a == "hard":
        hard()
    else:
        print("invalid option")
    r=input("do you want to play again?")
    if r=="yes":
        number_guessing_project()
number_guessing_project()