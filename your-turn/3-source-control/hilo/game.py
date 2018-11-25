import random

print('---------------------------------')
print('   GUESS THAT NUMBER GAME')
print('---------------------------------')
print()

min_value = 0
max_value = 100
the_number = random.randint(min_value, max_value)
guess = -1
guess_count = 0

name = input('Player what is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between {} and {} (eg {}): '.format(min_value, max_value, the_number))
    guess = int(guess_text)
    guess_count += 1

    if guess < the_number:
        print('Sorry {}, your guess of {} was too LOW.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, your guess of {} was too HIGH.'.format(name, guess))
    else:
        print('Excellent work {}, you won after {} guess(es). It was {}!'.format(name, guess_count, guess))

print('bye bye')
