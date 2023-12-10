import random
import string
import PySimpleGUI as sg
import os
import keyboard

l1 = sg.Text("Password Length:", key="password", justification='left')
firstNum = 1
passLengthNum = sg.Text(firstNum, key="passLen") 
displayError = sg.Text("", key='error')
displayMessage = sg.Text("", key='message')
includeSymsBox = sg.Text("", key="syms")

layout = [[l1, passLengthNum, sg.Button("+"), sg.Button("-")],
          [displayError, displayMessage],
          [includeSymsBox],
    [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    elif event == "+":   
        firstNum += 1
        window["passLen"].update(firstNum)
    elif event == "-":
        firstNum -= 1
        window["passLen"].update(firstNum)
        if firstNum < 0:
                firstNum = 0
                window['error'].update("Cannot go lower than 0.")
                window["passLen"].update(firstNum)
    
    window['message'].update("Press OK or the Enter key to proceed")

    #if event == 'OK' or event == (keyboard.read_key() == "enter"):
        #()
    
"""
    if event == 'OK' or event == (keyboard.read_key() == "enter"):
        addSyms = sg.InputText(("Would you like to add symbols? y/n: "), enable_events=True).lower()
        window['syms'].update(addSyms)
        print("\n")
        if addSyms.isdigit():
            print("Please enter y or n.")
            continue
        else:
            pass 
"""
            
window.close()
