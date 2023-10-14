import random
import string

print("Password Generator\n")

allChars = list(string.printable)
allChars[-6:] = [] # remove items like \n \t \r \x0b \x0c and ' '

while True:
    passStrength = input("Enter the length of password: ")
    if passStrength.isdigit(): # .isdigit() checks to see if the input is an integer
        False
        break
    else:
        print("Please enter a integer to determine length.\n")
        continue

while True:
    addSyms = input("Would you like to add symbols? y/n: ").lower()
    if addSyms.isdigit():
        print("Please enter y or n.")
        continue
    else:
        pass 

    if addSyms == "y":
        pass
        False
    elif addSyms == "n":
        allChars[-32:] = []
        False
    else:
        print("Please enter y or n.")
        continue
    break

addNums = input("Would you like to add numbers? y/n: ").lower()
if addNums == "y":
    pass
elif addNums == "n":
    allChars[:10] = []

def randPassword():
    passwordAsList = []
    random.shuffle(allChars) # shuffles all the items in the list randomly
    for i in range(int(passStrength)):
        passwordAsList.append(allChars[i])
    newPassword = ''.join(passwordAsList) # .join() joins the list items together to create a string

    print(f"Your password is: {newPassword}")

randPassword() 