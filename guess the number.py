import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, wrong guess. Too low.')
        elif guess > random_number:
            print('Sorry, wrong guess. Too high.')
        
                      
    print(f'Yay! You guessed it correct. Congrats. You guessed the number {random_number}.')

guess(100)


import random
def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c': 
        guess = random.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)?').lower()
        if feedback == 'h': 
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'The computer has guessed your number {guess} correctly. Good job')

computer_guess(100)