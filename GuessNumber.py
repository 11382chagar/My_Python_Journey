import random

number = random.randint(1, 100)
print('Guess a number between 0 and 100')
guess = -1

while guess != number:
    guess = int(input('Enter your guess: '))
    if guess == number:
        print('You got it! The number is',number)
    elif guess > number:
        print('Your guess was too high, try again.')
    else:
        print('Your guess was too low, try again.')
