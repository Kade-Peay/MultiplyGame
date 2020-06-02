#!/bin/env python
import random

def getNumbers():
    num = random.randint(1,10)
    return num

if __name__ == "__main__":
    num1 = getNumbers()
    num2 = getNumbers()
    print(f'What is {num1} multiplied by {num2}?')
    guess = input('Guess: ')
    
    answer = num1 * num2

    if int(guess) == answer:
        print('You are correct!')
        print(f'{num1} multiplied by {num2} is = {answer}')
    else:
        print('You are incorrect...')
        print(f'{num1} multiplied by {num2} is = {answer} not {guess}')