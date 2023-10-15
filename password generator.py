import random
import string

print("Password Generator\n")

allChars = list(string.printable)
allChars[-6:] = [] # remove items like \n \t \r \x0b \x0c and ' '
allCharsNums = ''.join(allChars[:10])
allCharsSyms = ''.join(allCharsNums[-32:])

while True:
    passLength = input("Enter the length of password: ")
    print("\n")
    if passLength.isdigit(): # .isdigit() checks to see if the input is an integer
        False
        break
    else:
        print("Please enter a integer to determine length.\n")
        continue

while True:
    addSyms = input("Would you like to add symbols? y/n: ").lower()
    print("\n")
    if addSyms.isdigit():
        print("Please enter y or n.")
        continue
    else:
        pass 

    if addSyms == "y":
        pass
    elif addSyms == "n":
        allChars[-32:] = []
    else:
        print("Please enter y or n.\n")
        continue
    break

while True:
    addNums = input("Would you like to add numbers? y/n: ").lower()
    print("\n")
    if addNums.isdigit():
            print("Please enter y or n.")
            continue
    else:
        pass

    if addNums == "y":
        pass
    elif addNums == "n":
        allChars[:10] = []
    else:
        print("Please enter y or n.")
        continue
    break

def randPassword():
    passwordAsList = []
    random.shuffle(allChars) # shuffles all the items in the list randomly
    for i in range(int(passLength)):
        passwordAsList.append(allChars[i])
    newPassword = ''.join(passwordAsList) # .join() joins the list items together to create a string
    newPasswordLen = len(newPassword)

    print(f"Your password is: {newPassword}")

    # this code determines the password strength, didn't know how to make it a function
    totalScore = 0

    if newPasswordLen <= 7:
        pass
    elif newPasswordLen >= 8 and newPasswordLen <= 14:
        totalScore += 1
    elif newPasswordLen >= 15:
        totalScore += 2

    if newPassword.find(allCharsSyms) != -1:
        totalScore += 2
    else:
        totalScore += 1
    if newPassword.find(allCharsNums) != -1:
        totalScore += 2
    else:
        totalScore += 1
    
    if totalScore <= 3:
        print("Your password it weak!")
    elif totalScore >= 4 and totalScore <= 5:
        print("Your password is okay.")
    elif totalScore >= 6:
        print("Your password is strong.")

randPassword() 