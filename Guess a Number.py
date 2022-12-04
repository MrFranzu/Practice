from random import randint

number = randint(1,99)
attempts = 0

print("<<< You have 5 attempts to guess, guess wisely? hahaha. >>>\n")
print("Choose a random number from 1-99")

while attempts != 5:
    guess = int(input("Make your guess: "))

    if guess > number:
        print("Wrong, make it lower!")
        attempts = attempts + 1
    elif guess < number:
        print("Wrong, make it higher!")
        attempts = attempts + 1
    else:
        print("Dang, you guess it right!!")
        exit()

print(f"I guess your not wise to guess? lol. The number is {number}")
