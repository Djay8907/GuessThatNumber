#GuessThatNumber
#A simple Python program that uses while loops and if statements to guess a secret number.
secret_number = 50
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You Won!')
        break
else:
    print('Sorry! You lose!')
