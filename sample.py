#login form
from tkinter import *
root=Tk()
root.geometry("500x300")

def getvals():
    print("Successfully logged in")

Label(root, text="LOGIN").grid(row=0,column=3)
username=Label(root,text="Username")
password=Label(root,text="Password")

username.grid(row=1,column=2)
password.grid(row=2,column=2)

usernamevalue=StringVar
passwordvalue=StringVar
checkvalue=IntVar

usernameentry= Entry(root,textvariable = usernamevalue)
passwordentry= Entry(root,textvariable = passwordvalue)

usernameentry.grid(row=1,column=3)
passwordentry.grid(row=2,column=3)

checkbtn=Checkbutton(text="Remember me",variable=checkvalue)
checkbtn.grid(row=3,column=3)

Button(text="Login",command=getvals).grid(row=4,column=3)


root.mainloop()
