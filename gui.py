import PySimpleGui as sg

label = sg.Text("Login App")
user_input = sg.Input(key="user")
password_input = sg.Input(key="password")
login_button = sg.Button("Login", key="login")