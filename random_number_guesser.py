# imports the random module
import random

# asks the user to input an integer for the start of the range
start = input("Enter the start of the range: ")
# starts a loop that run if the user does not enter an integer
# the loop will continue until the user inputs a valid integer
while not start.isdigit():
    print("Enter a valid number")
    start = input("Enter the start of the range: ")
# asks the user to input an integer for the end of the range
end = input("Enter the end of the range: ")
# starts a loop that run if the user does not enter an integer
# the loop will continue until the user inputs a valid integer,
# that is greater than the start integer
while not end.isdigit() or int(end) < int(start):
    print("Enter a valid number.")
    end = input("Enter the end of the range: ")
# creates a variable to store the random number generated
# from the start and end range
random_number = random.randint(int(start), int(end))

# create a variable to store the guess
guess = None
# create a variable to store the number of attempts
attempts = 0

# create a loop that starts if the guess is != to the random number
while guess != random_number:
    # creates a variable called guessed_number
    # that takes user input for the value
    guessed_number = input("Guess a number. ")
    # creates an if statement that checks if the guessed number is an integer
    if not guessed_number.isdigit():
        # prompts the user to enter a valid number, if the
        # if statement above was executed
        print("Please enter a valid number.")
        # to continue starts the code block over,
        #without incrementing the iterations
        continue
    # iterates the attempts by 1
    attempts += 1
    # makes sure the guesses_number is an integer
    # and stores it in the guess variable
    guess = int(guessed_number)
# creates a variable called suffix with an empty string
suffix = ""
# statement runs if attempts are > 1
if attempts > 1:
    # if attempts are greate than 1, the empty string in the suffix variable
    # is replaced with an s
    suffix = "s"
# prints out the number of attempts, it took to guess the rand int
# the f statement calls in the values of {attempts} and {suffix}
print(f"You guessed the number in {attempts} attempt{suffix}.")
