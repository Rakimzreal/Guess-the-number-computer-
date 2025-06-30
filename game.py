import random


def guess():
    while True:
        x = int(input('Enter a maximum value: '))
        random_number = random.randint(1, x)
        guess = 0
        attempts = 0
        while guess != random_number:
            guess = int(input(f'Guess a number between 1 and {x}: '))
            attempts +=1
            print(f'Tries: ', attempts)
            if guess < random_number:
                print('Try again, Too low! ')
            elif guess > random_number:
                print('Try again, Too high! ')

        print(f'You guessed the number {random_number} correctly!! ')

        choice = input('Restart? (yes/no): ').lower().strip()
        if choice != 'yes':
            break
    
guess()