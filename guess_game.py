import random
from enum import Enum



def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        
        try:
            guess = int(input(f"Guess a number between 1 and {x}: \n"))
            if guess <= 0 | guess >= x:
                print("Please enter a number between 1 and 10: \n")
            else:
                if guess < random_number:
                    print("Sorry, guess again, Too low.")
                elif guess > random_number:
                    print("Sorry, guess again. Too high")
        except ValueError:
            print("Please enter a number")

    print(f"You have guessed the number {random_number} correctly!")
    
def computer_guess(x):
    low = 1
    high = x
    feedback = Enum('feedback', 'H L C')
    while feedback != 'C':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high.
        feedback = input(f'Is {guess} Too high , too low , or correct (H/L/C)?')
        if feedback == 'H':
            high = guess - 1
        elif feedback == 'L':
            low = guess + 1
    print(f"yay! the computer guessed your number, {guess}, correctly!")

# guess(10) 

# A function to ask the user to choose between guessing a number or having the computer guess a number

def choose():
    print("Would you like to: \n 1. guess a number or, \n 2. have the computer guess a number? \n")
    choice = input("Please enter 1 or 2: \n")
    if choice == "1":
        guess(10)
    elif choice == "2":
        computer_guess(10)
    else:
        print("Please choose either guess or computer")
        choose()

if __name__ == "__main__":
    choose()
