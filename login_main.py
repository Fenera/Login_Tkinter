#import Tk module
import tkinter

#creates window
screen = tkinter.Tk()

#titles the window
screen.title('Login Page')

#set initial dimensions of the screen
screen.geometry('540x720')

#set background(fg = font color, bg = background color)
screen.config(bg='#fa9247')

frame = tkinter.Frame(bg = '#fa9247' )

#example password and username
ex_username = "johndoe73"
ex_password = "password1234"

def confirm_info(username, password):
    return username == ex_username and password == ex_password

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if confirm_info(username, password):
        print("Welcome to Email")
    
    else:
        print("Incorrect Information! Try Again.")


    

#Creating widgets
login_label = tkinter.Label(frame, text = "Login", bg='#fa9247', fg = '#5f92ff', font = ("Arial", 30))
username_label = tkinter.Label(frame, text = "User Name", bg='#fa9247', font = ("Arial", 16))
username_entry = tkinter.Entry(frame, font = ("Arial", 16))
password_entry = tkinter.Entry(frame, show = "*", font = ("Arial", 16))
password_label = tkinter.Label(frame, text = "Password", bg='#fa9247', font = ("Arial", 16))
login_button = tkinter.Button(frame, text = "Login", bg = "#5f92ff", fg = "#FFFFFF", font = ("Arial", 16), command=login)


#Place widgets on screen(sticky = take up space in N, E, W, S)
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady = 30)
username_label.grid(row=1, column = 0)
username_entry.grid(row=1, column=1, pady = 20)
password_label.grid(row = 2, column = 0)
password_entry.grid(row = 2, column=1, pady = 20)
login_button.grid(row=3, column=0, columnspan=2, pady = 10)

frame.pack()
screen.mainloop()

