import random


numToGuess = int(input('Enter the number the computer has to guess:'))

def guessingGame(num):
    guessedNum = random.randint(1,numToGuess)
    computerGuess = False

    while computerGuess != True:
       if guessedNum == num:
           print('%d is correct!' % guessedNum)
           computerGuess = True
       else: 
            print('%d is not correct! Guess again!' % guessedNum)
            guessedNum = random.randint(1,numToGuess)
    
    # O(n)
    # for guessedNum in range(1,10):
    #     if guessedNum != num:
    #         print('%d is not correct! Guess again!' % guessedNum)
    #         guessedNum += 1
    #     else:
    #         return('That is correct! You guessed %d and the number was %d!' % (guessedNum, num))
    

guessingGame(numToGuess)