from random import randint
x = randint(0,300)
for count in range(0,10):
    print("input a number between 0 and 300")
    a = input()
    digit = int(a)
    if digit == x:
        print("bingo!")
    elif digit > x:
        print("It's too big")
    else:
        print("It's too small")

