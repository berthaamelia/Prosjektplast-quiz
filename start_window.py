import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from subprocess import call

#Defining all sub-routines
def play():
    call(["python", "Quiz_final.py"])

#Make Welcome GUI
main= Tk()
main.title("Prosjektplast")
main.configure(background= "#D5F5E3")
main.geometry("1000x200")

#main.bgpic= ("C:/Users/berthaamelia/Documents/Prosjektplast/Hersleb_skole_project/prosjektplast.jpg")

#Adding a frame
GUIFrame=Frame(main)
GUIFrame.pack()

#Adding a Label
Label(main, text="Welcome! Click start to play the quiz", font="arial 20 bold").pack()

#Add start button
Button(GUIFrame, text = "Start", width=15, height=3, command=play).pack()
#Button(GUIFrame, text = "Norsk", width=12, command=play).grid(row=1, column=1, sticky=W)

#Create start button
button_start = tk.Button()

#play all functions above
main.mainloop()
