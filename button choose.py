from tkinter import *
from tkinter import Tk
import tkinter as tk
def base():
  def login():
    from both import login
    MusicPlayer(root)
  def signin():
    from both import signin
  
  root=Tk()
  #
  root.title("in you goo")
  root.geometry("400x400")
  # Disable resizing
  root.resizable(False,False)
  # Frame for radio buttons
  dark=PhotoImage(file='E:/cs/final/real/dark.png')
  blood=PhotoImage(file='E:/cs/final/real/blood.png')
  buttonframe = LabelFrame(root,text="Choose A Theme",bg="lavender",fg="black",bd=5,relief=FLAT)
  buttonframe.place(x=0,y=0,width=400,height=400)
      # Inserting Play Button
  default_btn = Button(buttonframe,image=dark,command=login,relief=FLAT, activebackground="#ff92ed").grid(row=0,column=5,padx=20,pady=15)
  bloody_btn = Button(buttonframe,image=blood,command=signin,relief=FLAT, activebackground="#ff92ed").grid(row=0,column=15,padx=10,pady=15)
  
  root.mainloop()
base()
