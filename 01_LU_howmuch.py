# Lucky Unicorn Decomposition Part 1
# Get initial amount and check that its valid


# Integer checking function
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Whoops! please enter an integer"

        try:
            response = int(input("Enter an integer between {} and {}  ".format(low, high)))

            if low <= response <= high:
                return response
            else:
                print("That number isn't between {} and {}!".format(low, high))
                print()
        except ValueError:
            print(error)
            print()

# main code

how_much = intcheck("How much money do you want to play with? ", 1, 10)