import random
import time
print("::ROCK ,PAPER & SCISSOR GAME::")
name1=input("ENTER YOUR NAME:")
n=int(input("ENTER HOW MANY ROUNDS DO YOU WANT TO PLAY?:"))
list1=["ROCK", "PAPER", "SCISSOR"]

i=0
c=0
h=0
for i in range(0,n):
    rand = random.choice(list1)

    choice=str(input("TYPE ROCK\PAPER\SCISSOR\n"))
    if choice==rand:
        print("TIE")
    elif rand=="ROCK" and choice=="PAPER":
        print(name1," WIN")
        h=h+1
    elif rand=="ROCK" and choice=="SCISSOR":
        print("COMP WIN")
        c=c+1
    elif rand=="PAPER" and choice=="SCISSOR":
        print(name1,"WIN")
        h=h+1
    elif rand=="PAPER" and choice=="ROCK":
        print("COMP WIN")
        c=c+1
    elif rand=="SCISSOR" and choice=="ROCK":
        print(name1,"WIN")
        h=h+1
    elif rand=="SCISSOR" and choice=="PAPER":
        print("COMP WIN")
        c=c+1
    comp=c
    hum=h

fgh=f"COMPUTER'S SCORE IS {comp}:"
jkl=f"{name1}'s score is {hum}:"
print(fgh)
print(jkl)
print("GAME OVER")

if comp>hum:
    print("\tCOMPUTER WIN")
    input()
elif comp<hum:
    print("\tYOU WIN")
    input()
else:
    print("DRAW")
    input()
