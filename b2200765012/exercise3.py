import random
n=random.randint(0,100)
guess = int(input("pick a number"))
while guess != n:
    if guess>n:
        guess= int(input("decrease your number"))
    else:
        guess= int(input("increase your number"))
print("Woow you found the number")