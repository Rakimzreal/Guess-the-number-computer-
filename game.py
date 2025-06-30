import random


def guess():
    x = int(input('Enter a maximum value: '))
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Try again, Too low! ')
        elif guess > random_number:
            print('Try again, Too high! ')

    print(f'You guessed the number {random_number} correctly!! ')
    
guess()