import random

print('Hello, What is your name?')
name = input()
secretNum = random.randint(1, 20)
print('Well, ' + name + ', I will chose a number between 1 and 20')

for guessesTaken in range(1, 6):
    print('Take a guess!')
    guess = int(input())

    if guess < secretNum:
        print('Your guess is low!')
    elif guess > secretNum:
        print('Your guess is high!')
    else:
        break

if guess == secretNum:
    print('Yes! You did it ' + name + ', You find the correct number.')
else:
    print('No! You fool ' + name + '! You didn\'t find.')