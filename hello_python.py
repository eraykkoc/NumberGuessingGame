import random

print("Welcome to Number Guessing Game")

number = random.randint(0,50)

usernumber = int(input("Enter a number between 0 and 50: "))

luck = 3
prize = 500

while True:
    if luck != 0:
        if usernumber > number:
            luck -= 1
            print(luck, "chance left")
            prize -= 50
            print(prize, "USD left!")
            usernumber = int(input("Enter a smaller number: "))
        elif usernumber < number:
            luck -= 1
            print(luck, "chance left")
            prize -= 50
            print(prize, "USD left!")
            usernumber = int(input("Enter a bigger number: "))

        if usernumber == number:
            if luck == 3:
                prize = prize * 10
            elif luck == 2:
                prize = prize * 5
            elif luck == 1:
                prize = prize * 3
            print("You won", prize, "USD. Congratulations!")
            break

        if luck == 1:
            print("Unfortunately, You lost!")
            break