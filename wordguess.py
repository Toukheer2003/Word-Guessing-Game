import tkinter as tk
import os
from tkinter import*
import sys

root=Tk()
root.title("WORD GUESS")
l1=Label(root,text='WELCOME TO WORD GUESS',fg='magenta4')
l1.pack()
def submit():
    name=name_var.get()
    print("Hi " + name)
     
l=tk.Label(root,text='Enter your name:',fg='black')
l.pack()
name_var=tk.StringVar()
e1=tk.Entry(root,textvariable = name_var,width=50)
e1.pack()

sub_btn=tk.Button(root,text = 'Submit', command = submit)
sub_btn.pack()

entry_text=tk.StringVar()
e=Entry(root,width=50,textvariable=entry_text)
entry_text.set('Click your choice of difficulty')
e.pack()
def easy():
    path="./easy.py"
    os.system(f" python {path}")
    
def hard():
    path="./hard.py"
    os.system(f" python {path}") 
      
def close():
    sys.exit(0)

b1=Button(text='Easy',command=easy)
b1.pack()
b2=Button(text='Hard',command=hard)
b2.pack()
b3=Button(text='Close',command=close)
b3.pack()

root.mainloop()


