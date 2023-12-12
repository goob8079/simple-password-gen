import random
import string
import PySimpleGUI as sg
import os
import keyboard

allChars = list(string.printable)
allChars[-6:] = [] # remove items like \n \t \r \x0b \x0c and ' '
allCharsNums = ''.join(allChars[:10]) # the numbers
allCharsSyms = ''.join(allChars[-32:]) # the symbols

l1 = sg.Text("Password Length:", justification='left')
l2 = sg.Text("Add Symbols?:", justification="left")
l3 = sg.Text("Add Numbers?:", justification="left")
firstNum = 1
passLengthNum = sg.Text(firstNum, key="passLen") 
displayError = sg.Text("", key='error')
displayMessage = sg.Text("Press OK to generate password", key='message')
includeSymsBox = sg.Text("", key="incSyms", justification="left")
includeNumsBox = sg.Text("", key="incNums", justification="left")
displayPassword = sg.Text("Your Password is:", key="dispPass", justification="left")

layout = [[l1, passLengthNum, sg.Button("+"), sg.Button("-")],
          [l2, sg.Button("y", key="symY"), sg.Button("n", key="symN")],
          [includeSymsBox], 
          [l3, sg.Button("y", key="numY"), sg.Button("n", key="numN")],
          [includeNumsBox],
          [displayMessage, displayError],
          [displayPassword],
    [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    
    if event == "+":   
        firstNum += 1
        window["passLen"].update(firstNum)
    elif event == "-":
        firstNum -= 1
        window["passLen"].update(firstNum)
        if firstNum < 1:
                firstNum = 1
                window['error'].update("Cannot go lower than 1.")
                window["passLen"].update(firstNum)

    if event == "symY":
        window["incSyms"].update("You choose: Yes")
    elif event == "symN":
        window["incSyms"].update("You choose: No")
        allChars[-32:] = []
  
    if event == "numY":
        window["incNums"].update("You choose: Yes")
    elif event == "numN":
        window["incNums"].update("You choose: No")
        allChars[:10] = []

    def randPassword():
        passwordAsList = []
        random.shuffle(allChars) # shuffles all the items in the list randomly
        for i in range(firstNum):
            passwordAsList.append(allChars[i])
        newPassword = ''.join(passwordAsList) # .join() joins the list items together to create a string
        
        window["dispPass"].update(f"Your Password is: {newPassword}")

    if event == 'OK':        
        randPassword()
    else:    
        continue

window.close()