import random
print("welcome to the number guess game!\n")
b = random.randrange(0, 5)
while True:
    a = int(input("enter any number range b/w (o to 10): "))
    if a == b:
        print("you are correct!")
        break
    elif a < b:
        print("you were below the number")
    else:
        print("you were above the number")
