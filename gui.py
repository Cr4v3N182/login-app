import PySimpleGUI as sg

actual_users= {"matt" : "asd"}

label = sg.Text("Enter your login and password")
user_info = sg.Text("Enter login:       ")
user_input = sg.Input(key="user")
pass_info = sg.Text("Enter password:")
password_input = sg.Input(key="password")
login_button = sg.Button("Login", key="login")
exit_button = sg.Button("Exit", key="exit")

layout = [[label], [user_info, user_input], [pass_info, password_input], [login_button, exit_button]]

window = sg.Window("Login app", layout=layout, element_justification='c')

while True:
    event, value = window.read()
    dict_users = {} #dictionary for the comparison
    match event:
        case "login":
            user = value['user']
            password = value['password']
            dict_users[user] = password     # holds user and password input.
            print(dict_users)
            if dict_users == actual_users:
                sg.popup("Acces granted.")
            else:
                sg.popup("Wrong username or password.")

        case "exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()