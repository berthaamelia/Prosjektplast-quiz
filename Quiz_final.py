import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from subprocess import call
import vlc
import time


#Questions
Qu= ["What type of plastic is a coca cola bottle?",
     "What type of plastic is a detergent container?",
     "Can we recycle plastic wrap?",
     "Some plastics contain BPA. Can using such plastics have a negative effect on people health?",
     "What type of plastic is styrofoam?",
     "Do you need to clean plastic container before you recycle it?",
     "Can we recycle black color plastic here in Norway?",
     "How long does it take for 1 plastic bottle to degrade?",
     "Can plastic kill fishes in the ocean?"]

Ans=["PET", "HDPE", "Yes", "Yes" , "PS", "Yes", "No", "450 years","Yes"]
Ch1=["PET", "PET", "Yes", "Yes", "PS", "Yes", "Yes", "250 years","Yes"]
Ch2=["HDPE", "HDPE", "NO", "NO", "PET", "No", "No", "450 years","NO"]
img_names=["bottle.jpg",'container.jpg','cling_wrap.jpg','BPA.jpg',
           'styrofoam.jpg','clean_dryPlastic.png',
           'blackColorbottle.jpg',
           "bottle1.png",'water_fish.jpg']
hits1=0
hits2=0
hit_tot= 1
score=0

#Starts music
def start_audio():
    sound_file = vlc.MediaPlayer ("file:///Users/berthaamelia/Documents/Prosjektplast/Hersleb_skole_quiz/bensound.mp3")
    sound_file.play()

start_audio()

def chk_answer(root,ans):

    global hit_tot, score
    if hit_tot < 9:
        #print(f' answer is : {ans}')
        #print(hit_tot)
        # chk score
        if ans == Ans[hit_tot-1]:
            score +=1
            print(f'{score}/9')
        #upadate quiz
        Quest['text'] = Qu[hit_tot]
        button1['text'] = Ch1[hit_tot]
        button2['text'] = Ch2[hit_tot]
        button3['text'] = f'Score\n{score}/9'
        image_n = Image.open(img_names[hit_tot])
        photo_n = ImageTk.PhotoImage(image_n)
        background_label.config(image=photo_n)
        background_label.image= photo_n

    elif hit_tot == 9:
        if ans == Ans[hit_tot - 1]:
            score += 1
            button3['text'] = f'Score\n{score}/9'
        if score >= 5:
            call(["python", "PP_slotmachine.py"])
        else:
            print(f'{score}/9')
            print('It is finished')
            print(f'Final score: {score}/9')
            root = tk.Tk()

            text2 = tk.Text(root, height=20, width=100)
            text2.tag_configure('big', font=('Verdana', 20, 'bold'))
            text2.insert(tk.END,'\nYou answered less than 5 correct answers\n', 'big')
            text2.insert(tk.END, 'Please try again.\n', 'follow')
            text2.pack(side=tk.LEFT)

            root.mainloop()
            tk.mainloop()


    else:
        print(f'{score}/9')
        print('It is finished')
        print(f'Final score: {score}/9')
        #button3['text'] = f'Score\n{score}/9'


    hit_tot += 1

height = 900
width = 1200

root = tk.Tk()
root.title('Prosjekt Plast Quiz')
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()


#frame for title
#frame_title = tk.Frame(root, bg='#99c2ff', bd=5)
frame_title = tk.Frame(root, bg='#ccffdd', bd=5)
frame_title.place(relx=0, rely=0, relwidth=1, relheight=0.1)

title = tk.Label(frame_title, bg='#ccffdd', text='Prosjekt Plast Quiz',  font=("Helvetica", 40))
title.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.8)
####frame for quiz buttons####
frameQ = tk.Frame(root,  bd=5)
frameQ.place(relx=0, rely=0.1, relwidth=1, relheight=0.1)
Quest= tk.Label(frameQ, bg='#ccffdd', text=Qu[0],  font=("Helvetica", 20))
Quest.place(relx=0.1, rely=0, relwidth=0.8, relheight=0.8)

####frame for quiz buttons####
#bg='#99c2ff',
frame = tk.Frame(root,  bd=5)
frame.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
button1 = tk.Button(frame,text=Ch1[0], bg='#99c2ff', font=("Helvetica", 20), command=lambda: chk_answer(root,button1['text']))
button1.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)
button2 = tk.Button(frame, text=Ch2[0], bg='#99c2ff', font=("Helvetica", 20), command=lambda: chk_answer(root,button2['text']))
button2.place(relx=0.6, rely=0, relwidth=0.2, relheight=1)

button3 = tk.Button(frame, text='Score\n0/9', bg='#ccccff', font=("Helvetica", 12))
button3.place(relx=0, rely=0, relwidth=0.1, relheight=0.6)


#image frame
frame2 = tk.Frame(root)
frame2.place(relx=0, rely=0.2, relwidth=1, relheight=0.6)

image = Image.open(img_names[0])
photo = ImageTk.PhotoImage(image)
background_label = tk.Label(frame2, image=photo)
background_label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
