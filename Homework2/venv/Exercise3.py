from random import randint

gameWon = False
tries = 10
randomNumber = randint(1,100)
print("Try to guess the secret number between 1 and 100.")
print("You have 10 tries to win the game!")
print()

while tries > 0:
    userInput = input("Input a number between 1 and 100 ")
    tries = tries - 1
    if int(userInput) > randomNumber:
        print("The number you entered is too high!")
    elif int(userInput) < randomNumber:
        print("The number you entered is too low!")
    elif int(userInput) == randomNumber:
        gameWon = True
        break
    print("Remaining tries - " + str(tries))

if gameWon == True:
    print("You won the game in " + str(tries) + " tries! :)")
elif gameWon == False:
    print("You lost the game! :(")