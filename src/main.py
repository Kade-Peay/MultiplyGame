#!/bin/env python
import random, sys

def getNumbers():
    num = random.randint(1,10)
    return num

def guess():
    num1 = getNumbers()
    num2 = getNumbers()
    print('"x" to exit\n')
    print(f'What is {num1} multiplied by {num2}?\n')
    guess = input('Guess: ')
    
    answer = num1 * num2

    if guess.lower() == 'x':
        sys.exit()
    elif int(guess) == answer:
        print('You are correct!')
        print(f'{num1} multiplied by {num2} is = {answer}\n')
    else:
        print('You are incorrect...')
        print(f'{num1} multiplied by {num2} is = {answer} not {guess}\n') 


if __name__ == "__main__":
    running = True
    while running:
        guess()