import random

comGuessNum=random.randint(0, 100);

while True:
    guessedNum = int(input(" your Guess between 0 to 100: "))
    if guessedNum>comGuessNum:
        print("Guess Lower")
    elif guessedNum<comGuessNum:
        print("Guess Higher")
    else:
        print(" Hurray!!... You Guessed correctly!!")
        break
