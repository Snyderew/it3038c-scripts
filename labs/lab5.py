import random

print("Guess a random number between 0 and 9")

myGuess = int(input())

randomNumber = random.randint(0,9)

while myGuess != randomNumber:

    if myGuess < randomNumber:

        print("Your guess is too low. Try again.")

        myGuess = int(input())


    else:
    
        print("Your guess is too high. Try again.")
    
        myGuess = int(input())


print("Good job! You guessed the number correctly. The random number is %s." % randomNumber)
