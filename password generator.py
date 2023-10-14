import random
import string

print("Password Generator\n")

allChars = list(string.printable)
allChars[-6:] = [] # remove items like \n \t \r \x0b \x0c
random.shuffle(allChars) # shuffles all the items in the list randomly

while True:
    passStrength = input("Enter the length of password (max limit = 93): ")
    if passStrength.isdigit(): # .isdigit() checks to see if the input is an integer
        False
        break
    else:
        print("Please enter a integer to determine length.\n")
        continue

def randPassword():
    passwordAsList = []
    for i in range(int(passStrength)):
        passwordAsList.append(allChars[i])
    newPassword = ''.join(passwordAsList) # .join() joins the list items together to create a string

    print(f"Your password is: {newPassword}")

randPassword()
