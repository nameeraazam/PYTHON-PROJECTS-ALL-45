import random

options = ["rock", "scissor", "paper"]

'''
rock vs paper -> paper wins
rock vs scissor -> rock wins
paper vs scissor -> scissor wins
'''

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
Game Start.........
1 Yes
2 NO | Exit
    '''))
    
    if uc == 1:
        for a in range(1, 6):
            userInput = int(input('''
1 Rock
2 Scissor
3 Paper
'''))

            if userInput == 1:
                uchoice = "rock"
            elif userInput == 2:
                uchoice = "scissor"
            elif userInput == 3:
                uchoice = "paper"
            else:
                print("Invalid input. Please choose 1, 2, or 3.")
                continue

            Cchoice = random.choice(options)
            
            print("Computer Value:", Cchoice)
            print("User Value:", uchoice)

            if uchoice == Cchoice:
                print("Game Draw")
                ucount += 1
                ccount += 1
            elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
                print("YOU WIN")
                ucount += 1
            else:
                print("Computer Win")
                ccount += 1
            
            print(f"Current Score - You: {ucount} | Computer: {ccount}")
        
        print("Game Over! Final Score:")
        print(f"You: {ucount} | Computer: {ccount}")
        


    else:
        break
