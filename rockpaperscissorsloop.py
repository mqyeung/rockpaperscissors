def rockPaperScissors():
    import random
    rpsArray, userInt = ["rock", "paper", "scissors"], "b"
    while userInt != "":
        compInt = random.randint(0,2)
        userInt = int(input("\nPlease input 0 for rock, 1 for scissors, 2 for paper. Press 'Enter' to exit. "))
        if compInt == userInt:
            print("\nYou tied! You picked", rpsArray[userInt], "and computer picked", rpsArray[compInt],".")
        elif (compInt - 1) % 3 == userInt:
            print("\nYou lost! You picked", rpsArray[userInt], "and computer picked", rpsArray[compInt],".")
        elif (compInt + 1) % 3 == userInt:
            print("\nYou won! You picked", rpsArray[userInt], "and computer picked", rpsArray[compInt],".")
rockPaperScissors()