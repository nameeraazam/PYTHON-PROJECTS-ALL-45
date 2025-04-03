import random 
# generate random number
number = random.randint(1, 100)

while True:
    guess = int(input("Enter your guess number: "))
    if guess < number:
        print("Too Low Number!")
    elif guess > number:
        print("Too High number!")
    else:
        print("Congratulations! You Got it Right!")
        break