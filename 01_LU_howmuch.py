# Ask user for number
# Loop question so that it repeats until valid number is entered
# Make code recyclable

# function goes here
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

num_1 = intcheck("Enter a number between 1 and 300", 1, 300)
num_2 = intcheck("Enter a number between 60 and 550", 60, 550)
