import random
import string
import PySimpleGUI as sg
import os
import keyboard

l1 = sg.Text("Enter Password Length:", key="password", justification='left')
passLengthInput = sg.InputText('', enable_events=True, key="-INPUT-", justification='left') 
displayError = sg.Text("", key='xxx')
displaySymsBox = sg.Text("", key="syms")

layout = [[l1, passLengthInput],
          [displayError],
          [displaySymsBox],
    [sg.Button('OK'), sg.Button('Cancel')]
]

window = sg.Window("Password Generator", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    passLength = int(values["password"])

    if passLengthInput == type(int):
        pass
    elif passLengthInput == '':
        window['xxx'].update("Please enter a integer to determine length.\n") # update() updates the variable of the key that is called, in this case it updates displayError
        continue
    elif passLengthInput != type(int):
        window['xxx'].update("Please enter a integer to determine length.\n")
        continue

    if event == 'OK' or event == (keyboard.read_key() == "enter"):
        addSyms = sg.InputText(("Would you like to add symbols? y/n: "), enable_events=True).lower()
        window['syms'].update(addSyms)
        print("\n")
        if addSyms.isdigit():
            print("Please enter y or n.")
            continue
        else:
            pass 

window.close()
