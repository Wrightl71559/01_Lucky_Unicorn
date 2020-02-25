# Lucky Unicorn fully working program
# Program should work - needs to be usability tested

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
    print

# Cost payout constants
COST = 1    #cost per round
UNICORN = 5
ZEB_HOR = 0.5
DONKEY = 0 # STUFF ISNT RIGHT HERE


# Introduction
print("** Welcome to the Lucky Unicorn Game **")
print()
print("To play, enter an amount of money between $1 & $10(whole dollars only)")
print()
print("It costs $1 per round")
print()
print("Payouts: ")
print("-Unicorn: +$5.00")
print("- Horse / Zebra: -$0.50")
print("-Donkey: -$1.00")


# main code

# Ask user how much they want to play with (min $1, max $10)
balance = intcheck("How much money would you like to play with? $", 1, 10)

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
    print("you got a {}.".format(token))

    # Adjust toal correctly for a given token
    if token == "unicorn":
        balance += 5    # wins $5
        feedback = "Congratulations you won $5.00"
    elif token == "donkey":
        balance -= 1    # loses $1
        feedback = "Sorry, you did not win anything this round"
    else:
        balance -= 0.5  # wins / loses 50c
        feedback = "You've won 50c"

    print()
    print (feedback)
    print("you have ${:.2f} to play with".format(balance))

    # If user has enough money to play, ask if they want to play again
    if balance < 1:
        print("Sorry, you don't have enough money to continue. Game over")
        keep_going = "end"
    else:
        keep_going = input("Press <enter> to play again or any key to quit")

# Farewell user at end of game.
print("Thank you for playing :)")



