#import Tk module
import tkinter

#creates window
screen = tkinter.Tk()

#titles the window
screen.title('Login Page')

#set initial dimensions of the screen
screen.geometry('540x720')

#set background(fg = font color, bg = background color)
screen.config(bg='#B3BEF4')

frame = tkinter.Frame(bg = '#B3BEF4')

#example password and username
ex_username = 'johndoe73'
ex_password = 'password1234'

def confirm_info(username, password):
    return username == ex_username and password == ex_password

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    if confirm_info(username, password):
        show_correct_text()
        print('Welcome to Email')
    
    else:
        show_incorrect_text()
        print('Incorrect Information! Try Again.')

def show_correct_text():
    correct_label.config(text = "Welcome back!")
    correct_label.grid(row = 2, column = 0, columnspan = 2, rowspan= 2, pady = 10)

    #remove text after 3 seconds(3000 millisecond)
    screen.after(3000, remove_incorrect_text)

def remove_correct_text():
    correct_label.config(text='')

def show_incorrect_text():

    incorrect_label.config(text='Incorrect Information! Try Again.')
    incorrect_label.grid(row=2, column = 0, rowspan=2, columnspan=2, pady = 10)

    #remove text after 1 second(1000 millisecond)
    screen.after(1000, remove_incorrect_text)

def remove_incorrect_text():
    incorrect_label.config(text='')

    

#Creating widgets
correct_label = tkinter.Label(frame, text = '', bg ='#B3BEF4', fg='#27C411', font = ('arial', 15) )
example_pw_label = tkinter.Label(frame, text= 'Username:johndoe73 \n Password: password1234',bg='#B3BEF4', fg = '#1a1a1a', font = ('Arial', 15))
incorrect_label = tkinter.Label(frame, text = '', bg ='#B3BEF4', fg='#F1441F' )
login_label = tkinter.Label(frame, text = 'Login', bg='#B3BEF4', fg = '#1A1A1A', font = ('Arial', 30), borderwidth=2, relief='solid')
username_label = tkinter.Label(frame, text = 'User Name', bg='#B3BEF4', font = ('Arial', 15))
username_entry = tkinter.Entry(frame, font = ('Arial', 15))
password_entry = tkinter.Entry(frame, show = '*', font = ('Arial', 15))
password_label = tkinter.Label(frame, text = 'Password', bg='#B3BEF4', font = ('Arial', 15))
login_button = tkinter.Button(frame, text = 'Login', bg = '#FFA765', fg = '#FFFFFF', font = ('Arial', 15), command=login)


#Place widgets on screen(sticky = take up space in N, E, W, S)
example_pw_label.grid(row=4, column=0, columnspan=2, pady = 20)
login_label.grid(row=0, column=0, columnspan=2, sticky='news', pady = 30)
username_label.grid(row=1, column = 0)
username_entry.grid(row=1, column=1, pady = 20)
password_label.grid(row = 2, column = 0)
password_entry.grid(row = 2, column=1, pady = 20)
login_button.grid(row=3, column=0, columnspan=2, pady = 10)

frame.pack()
screen.mainloop()

