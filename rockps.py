import random
import time

import os
while True:


    print("""\t\t::ROCK ,PAPER & SCISSOR GAME::""")
    time.sleep(.5)
    date1=time.asctime(time.localtime(time.time()))
    print("\t",date1)
    list1=["ROCK", "PAPER", "SCISSOR"]
    time.sleep(.5)
    i=0
    c=0
    h=0
    print("1.Play\n2.Leaderboard\n3.Exit")
    choose=int(input())
    os.system('cls')
    if choose==1:
        time.sleep(.4)
        name1=str.upper(input("ENTER YOUR NAME:"))

        n=int(input("ENTER HOW MANY ROUNDS DO YOU WANT TO PLAY?:"))
        os.system('cls')
        print("GAME STARTED CHOOSE ROCK PAPER OR SCISSOR( ͡° ͜ʖ ͡°)")

        for i in range(0,n):
            rand = random.choice(list1)

            shortcut=str(input("TYPE R\P\S\n"))
            if shortcut=="R" or shortcut=="r":
                choice="ROCK"
            elif shortcut=="P" or shortcut=='p':
                choice="PAPER"
            elif shortcut=="S" or shortcut=="s":
                choice="SCISSOR"


            if choice==rand:
                print("TIE")
            elif rand=="ROCK" and choice=="PAPER":
                print(name1," WON THIS ROUND")
                h=h+1
            elif rand=="ROCK" and choice=="SCISSOR":
                print("COMP WON THIS ROUND")
                c=c+1
            elif rand=="PAPER" and choice=="SCISSOR":
                print(name1,"WON THIS ROUND")
                h=h+1
            elif rand=="PAPER" and choice=="ROCK":
                print("COMP WON THIS ROUND")
                c=c+1
            elif rand=="SCISSOR" and choice=="ROCK":
                print(name1,"WON THIS ROUND")
                h=h+1
            elif rand=="SCISSOR" and choice=="PAPER":
                print("COMP WON THIS ROUND")
                c=c+1
            comp=c
            hum=h

        fgh=f"COMPUTER'S SCORE IS {comp}:"
        jkl=f"{name1}'s score is {hum}:"
        print(fgh)
        print(jkl)
        print("GAME OVER")
        score=open("rockps.txt","a")
        score.write(f"{name1}: {hum}\n")
        score.close()

        if comp>hum:
            print("\tCOMPUTER WIN")
            input()
        elif comp<hum:
            print("\tYOU WIN")
            input()
        else:
            print("DRAW")

            input()
        os.system('cls')

    elif choose==3:
        time.sleep(1)
        print("BYE BYE FELLA")
        time.sleep(.3)

        exit()

    elif choose==2:
         time.sleep(.4)
         score=open("rockps.txt","rt")
         me=score.read()
         print(me)
         score.close()
         input()
         os.system('cls')