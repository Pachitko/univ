import PySimpleGUI as sg
import os
from os.path import isfile, join

cwd = os.getcwd()

layout = [[sg.Button(button_text="OK")], [sg.Text(cwd)], [sg.Listbox(os.listdir(cwd), size=(
    40, 10), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, key='lb', enable_events=True)]]

window = sg.Window("File Explorer", layout)
lb = window['lb']

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()
