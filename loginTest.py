#import keyboard
#import asyncio
from tkinter import *
from functools import partial
#from multiprocessing import Process


#async def quitProgram():
#    if keyboard.wait("enter"):
#        exit()

#loop = asyncio.get_event_loop()
#loop.run_until_complete(quitProgram())
#loop.close()

i=0


def validateLogin(username, password):
    #print("username entered :", username.get())
    #print("password entered :", password.get())
    print("username entered :", username.get())
    print("password entered :", password.get())
    tkWindow.destroy()
    
    
#window
tkWindow = Tk()
tkWindow.attributes("-topmost", True)  
tkWindow.geometry('400x150')
tkWindow.tk.call(('tk', 'scaling', 2.1))  
tkWindow.title('Login e senha do Insight')
#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)
#if sair == True:
#    exit()
#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  
validateLogin = partial(validateLogin, username, password)
#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=1)
tkWindow.mainloop()
    #sair = False
    #if keyboard.is_pressed("enter"):
    #    sair = True
#elif keyboard.read_key("enter"):
#    exit()