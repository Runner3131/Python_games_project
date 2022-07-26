import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess =  input(f"Guess a number between 1 and {x}")
        if guess < random_number:
            print("Sorry, guess again, Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high")
    
    print(f"You have guessed the {random_number} number")
    
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high.
        feedback = input(f'Is {guess} Too high {H}, too low {L}, or correct {C}')
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
    print(f"yay! the computer guessed your number, {guess}, correctly!")

guess(10) 