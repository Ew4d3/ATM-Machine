#doesnt work but i watched a video to get me to this point lol

from tkinter import *
import os

def register_user():

    username_info = username.get()
    password_info = password.get()

    file=open(username_info, "w")
    file.write(username_info+"/n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text = "Registration successful", fg = "green", font = ("Calibri", 11)).pack()

def login_verify():
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            print("login success")
        else:
            print("password has not been recognised")
    else:
        print("User not found !")

    
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Button(screen1, text = "Register", width = 10, height = 1, command = register_user).pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()
    
    global username_entry1
    global password_entry1
    
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "").pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Label(screen2, text = "").pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()

def main_screen():
    global screen
    screen =  Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", width = "30", height = "2", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", width = "30", height = "2", command = register).pack()

    screen.mainloop()

main_screen()

