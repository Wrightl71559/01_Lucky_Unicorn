# Lucky unicorn decomposition sdtep 2
# Generate random tokens




import random

HOW_MUCH =100
tokens = ["horse", "horse", "horse",
          "zebra", "zebra", "zebra",
          "donkey", "donkey", "donkey", "unicorn"]


uni_count = 0
zh_count = 0
donk_count = 0

for item in range (0,HOW_MUCH):

    chosen = random.choice(tokens)

    if chosen == "unicorn":
        uni_count += 1
    elif chosen == "donkey":
        donk_count += 1
    else:
        zh_count += 1


    print(chosen)

# Money calculations
winnings = uni_count * 5 + zh_count *0.5

print("**** Win / Loss Calculations*****")
print("# Unicorns: {}".format(uni_count))
print("# Zebra / Horses: {}".format(zh_count))
print("# Donkeys: {}".format(donk_count))

print()
print("You spent ${}".format(HOW_MUCH))
print("You go home with ${:.2f}".format(winnings))

