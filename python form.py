#print("LOGIN")
#print("\n")
#username=input("USERNAME: ")
#password=input("PASSWORD: ")
#if username==" " or len(username)<6:
#   print("Invalid username")
#if password==" " or len(password)<6:
#    print("Invalid password")
#print("1. LOGIN")
#print("2. RESET")
#s=int(input())
#if s==1:
#   print("Welcome",username)
#elif s==2:


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
