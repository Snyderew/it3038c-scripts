import random

print("Guess a random number between 0 and 9.")

myGuess = int(input())

randomNumber = random.randint(0,9)

while myGuess != randomNumber:

    if myGuess < randomNumber and myGuess >= 0:
        print("Your guess is too low. Try again.")

        myGuess = int(input())

    elif myGuess > randomNumber and myGuess <= 9:
    
        print("Your guess is too high. Try again.")
    
        myGuess = int(input())

    elif myGuess < 0:

        print("You guessed a negative number. Please enter a number between 0 and 9.")

        myGuess = int(input())

    elif myGuess > 9:

        print("You guessed a number higher than 9. Please enter a number between 0 and 9.")

        myGuess = int(input())

    else:

        print("That is not a number. Please enter a number between 0 and 9.")

        myGuess = int(input())

print("Good job! You guessed the number correctly. The random number is %s." % randomNumber)
