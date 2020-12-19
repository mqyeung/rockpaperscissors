def rockPaperScissors():
    import random
    rpsArray, compInt, userInt = ["rock", "paper", "scissors"], random.randint(0,2), int(input("Please input 0 for rock, 1 for scissors, 2 for paper."))
    if compInt == userInt: 
        print("You tied! You picked", rpsArray[userInt], "and computer picked", rpsArray[compInt], ".")
    elif (compInt - 1) % 3 == userInt: 
        print("You lost! You picked", rpsArray[userInt], "and computer picked", rpsArray[compInt], ".")
    elif (compInt + 1) % 3 == userInt: 
        print("You won! You picked", rpsArray[userInt], "and computer picked", rpsArray[compInt], ".")
    return
rockPaperScissors()