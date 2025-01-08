
import random

myFavoriteNumber = random.randint(0, 20)
previousGuess = None

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

while True:
    guess = input("Guess my favorite number? ")

    if str(guess) == str(myFavoriteNumber):
        print(bcolors.OKGREEN + "YOU GUESSED MY FAVORITE NUMBER!!! YAY!" + bcolors.ENDC)
        exit()
    else:
        print("You FAIL!")
        # print(previousGuess)
        if previousGuess is not None:
            # print(previousGuess)
            if abs(int(guess)-myFavoriteNumber) < abs(int(previousGuess)-myFavoriteNumber):
                print(bcolors.FAIL + "warmer" + bcolors.ENDC)
            else: 
                print(bcolors.OKBLUE + "colder" + bcolors.ENDC)
    previousGuess = guess
# kids = [
#     "Bells McGee",
#     "Winnie",
#     "Han Solo",
#     "Josie"
# ]

# no_Ns = []

# for each_kid in kids:
#     no_Ns.append(each_kid.replace("n", "M"))

# for each_kid in no_Ns:
#     print(f"Hello, {each_kid}!")
