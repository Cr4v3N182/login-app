import PySimpleGUI as sg

label = sg.Text("Enter your login and password")
user_info = sg.Text("Enter login:       ")
user_input = sg.Input(key="user")
pass_info = sg.Text("Enter password:")
password_input = sg.Input(key="password")
login_button = sg.Button("Login", key="login")
exit_button = sg.Button("Exit", key="Exit")

layout = [[label], [user_info, user_input], [pass_info, password_input], [login_button, exit_button]]

window = sg.Window("Login app", layout=layout, element_justification='c')

while True:
    event, value = window.read()
    match event:


        case sg.WIN_CLOSED:
            break

window.close()