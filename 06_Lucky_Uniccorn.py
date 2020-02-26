# Lucky Unicorn fully working program
# Program should work - needs to be usability tested
# has been usability tested

import random

# Integer checking function below


def intcheck(question, low, high):
    valid = False
    error = "Whoops! please enter an integer"
    while not valid:
       try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print("That number isn't between {} and {}!".format(low, high))
                print()
       except ValueError:
           print(error)

# function to format responses based on token won


def token_statement(statement, char):
    print()
    print(char*len(statement))
    print(statement)
    print(char*len(statement))


# Introduction
print("** Welcome to the Lucky Unicorn Game **")
print()
print("* To play, enter an amount of money between $1 & $10(whole dollars only) *")
print()
print("* It costs $1 per round *")
print()
print("* Payouts: *")
print("* - Unicorn: +$5.00 *")
print("* - Horse / Zebra: -$0.50 *")
print("* - Donkey: -$1.00 *")


# main code

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money would you like to play with? $", 1, 10)

print()
print("** GAME STARTING **")

keep_going = ""
while keep_going == "":

    # Tokens list includes 10 items to prevent too many unicorns being chosen
    tokens = ["horse", "horse", "horse",
              "zebra", "zebra", "zebra",
              "donkey", "donkey", "donkey", "unicorn"]

    # Randomly choose a token from our list above
    token = random.choice(tokens)
    print()

    # Adjust total correctly for a given token
    if token == "unicorn":
        balance += 5    # wins $5
        token_statement("**** Congratulations it's a Unicorn!! You won $5.00 ****", "*")
    elif token == "donkey":
        balance -= 1    # loses $1
        token_statement("--- Sorry, it's a Donkey. You did not win anything this round ---", "-")
    else:
        balance -= 0.5  # wins / loses 50c
        token_statement("<<< Nearly. It's a {}. You won back 50c >>>".format(token), "^")

    print()
    print("You have ${:.2f} left to play with".format(balance))
    print()

    # If user has enough money to play, ask if they want to play again
    if balance < 1:
        print("Sorry, you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

# Farewell user at end of game.
print("Thank you for playing :)")



