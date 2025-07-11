import tkinter as tk
from tkinter import ttk

courses={
    "Btech":{
        "Computer science": "Covers programming and computer systems","Electronics":"Focuses on circuits & communication","Electrical":"Involves electricity and power systems","Mechanical":"Studies machines and engines"
        }
    }
root=tk.Tk()
root.title("Courses and Branch Info")
root.geometry("600x600")
tk.Label(root,text="Courses").pack()
course_var=tk.StringVar()
course_dropdown=ttk.Combobox(root,textvariable=course_var,state="readonly")
course_dropdown['values']=list(courses.keys())
course_dropdown.pack()
branch_var=tk.StringVar()
branch_dropdown=ttk.Combobox(root,textvariable=branch_var,state="readonly")
branch_dropdown.pack()
description_label=tk.Label(root,text=" ",wraplength=300)
description_label.pack()
def sb(event):
    course=course_var.get()
    branch_dropdown['values']=list(courses[course].keys())
    branch_dropdown.set("")
description_label.config(text="")
def sd(event):
    course=course_var.get()
    branch=branch_var.get()
    desc=courses[course][branch]
    description_label.config(text=desc)
course_dropdown.bind("<<ComboboxSelected>>",sb)
branch_dropdown.bind("<<ComboboxSelected>>",sd)
root.mainloop()
    
