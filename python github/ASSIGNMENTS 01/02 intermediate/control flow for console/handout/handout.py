#import random
#
#def play_high_low_game():
#    """
#    Play a game where the user guesses if their number is higher or lower than a random computer number.
#    """
#    print("\n**Welcome to the High-Low Game!**")
#    print("--------------------------------\n")
#    
#    score = 0
#    rounds = 5
#    
#    for round_num in range(1, rounds + 1):
#        print(f"**Round {round_num}**")
#        
#        # Generate random numbers
#        user_number = random.randint(1, 100)
#        computer_number = random.randint(1, 100)
#        
#        print(f"Your number is {user_number}")
#        
#        # Get user's guess
#        while True:
#            guess = input("Do you think your number is higher or lower than the computer's?: ").lower().strip()
#            if guess in ["higher", "lower"]:
#                break
#            print("Please enter either 'higher' or 'lower'.")
#        
#        # Check if guess is correct
#        if guess == "higher" and user_number > computer_number:
#            print(f"You were right! The computer's number was {computer_number}")
#            score += 1
#        elif guess == "lower" and user_number < computer_number:
#            print(f"You were right! The computer's number was {computer_number}")
#            score += 1
#        elif user_number == computer_number:
#            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
# #       else:
#            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
#        
#        print(f"Your score is now {score}\n")
#    
#    print("**Thanks for playing!**")
#    print(f"**Final Score: {score}**\n")
#    
#    return score
#
#if __name__ == "__main__":
#    play_high_low_game()




## Milestone #2: Get the user choice
#
## Display welcome message
#print("Welcome to the High-Low Game!")
#print("--------------------------------")
#
## Computer's and user's number
#computer_number = 7
#user_number = 17
#
## Display both numbers
#print(f"The computer's number is {computer_number}")
#print(f"Your number is {user_number}")
#
## Get user's guess (whether their number is higher or lower)
#user_choice = input("Do you think your number is higher or lower than the computer's?: ").lower()
#
## Check if the user's guess is correct
#if user_choice == 'higher' and user_number > computer_number:
#    print("SOLVED IT! Your number is indeed higher than the computer's.")
#elif user_choice == 'lower' and user_number < computer_number:
#    print("SOLVED IT! Your number is indeed lower than the computer's.")
#else:
#    print("Try again! Your guess doesn't match the actual comparison.")
#


#game logic
# Milestone #3: Write the game logic

# Display welcome message
#print("Welcome to the High-Low Game!")
#print("--------------------------------")
#
## Computer's and user's number
#computer_number = 79
#user_number = 3
#
## Display both numbers
#print(f"The computer's number is {computer_number}")
#print(f"Your number is {user_number}")
#
## Get user's guess (whether their number is higher or lower)
#user_choice = input("Do you think your number is higher or lower than the computer's?: ").lower()
#
## Check the conditions to determine who wins
#if user_number == computer_number:
#    print("The numbers are the same! The computer wins.")
#elif user_choice == 'higher' and user_number > computer_number:
#    print(f"You were right! Your number ({user_number}) is higher than the computer's number ({computer_number}).")
#elif user_choice == 'lower' and user_number < computer_number:
#    print(f"You were right! Your number ({user_number}) is lower than the computer's number ({computer_number}).")
#else:
#    print(f"You were wrong! The computer's number was {computer_number}, and your number was {user_number}.")
#

#4: Play multiple rounds
# Milestone #4: Play multiple rounds of the game

# Define the number of rounds
NUM_ROUNDS = 3  # You can change this to any number of rounds you'd like

# Display welcome message
print("Welcome to the High-Low Game!")
print("--------------------------------")

# Loop through the rounds
for round_number in range(1, NUM_ROUNDS + 1):
    print(f"\nRound {round_number}")

    # Generate the computer's number and the user's number for each round
    computer_number = 23  # This could be randomly generated for more variability
    user_number = int(input("Your number is: "))  # Let user input their number
    
    # Get the user's guess (whether their number is higher or lower)
    user_choice = input("Do you think your number is higher or lower than the computer's?: ").lower()

    # Check the conditions to determine who wins
    if user_number == computer_number:
        print("The numbers are the same! The computer wins.")
    elif user_choice == 'higher' and user_number > computer_number:
        print(f"You were right! Your number ({user_number}) is higher than the computer's number ({computer_number}).")
    elif user_choice == 'lower' and user_number < computer_number:
        print(f"You were right! Your number ({user_number}) is lower than the computer's number ({computer_number}).")
    else:
        print(f"Aww, that's incorrect. The computer's number was {computer_number}.")
    
    # Blank line to separate rounds visually
    print("\n")

