# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 11:09:47 2021

@author: hjkmo
"""

from tkinter import *
import time

from PIL import Image, ImageDraw
from matplotlib import animation

from playsound import playsound
from threading import Thread

def dancetoggle():
    global dancesw
    
    if dancesw: #if already paused
        dancesw=False #resume
        dancebutton['text'] = 'Dance'
    else: #if not paused
        dancesw=True
        dancebutton['text'] = 'Stop Dancing'
        dancing(Rtarm)         

def move_part(part, x, y):   
    part = msm.create_line(cx,cy, cx+30+x,cy-20+y, width=2)
    
def delmsm(part):
    msm.delete(part) 

def play_sound():
    playsound('GangnamStyle.mp3')
        
def dancing(part):
    global wavesw
    delmsm(part)
    
    thread = Thread(target=play_sound, daemon = True)
    thread.start()
        
    while dancesw == True:     
        if wavesw:
            newpart = msm.create_line(cx,cy, cx+30-5,cy-20-5, width=2)
            mw.update()
            wavesw=False
            delmsm(newpart)
        else:
            newpart = msm.create_line(cx,cy, cx+30,cy-20, width=2)
            mw.update()
            wavesw=True
            delmsm(newpart)
        time.sleep(1)
    else:
        Rtarm = msm.create_line(cx,cy, cx+30,cy-20, width=2)
        

mw = Tk()
mw.geometry('200x300')
title = Label(mw, text="Dancing Figure",bg="green",font=("bold",10))
title.pack()

dancesw=False
wavesw=True
dancebutton = Button(mw,text='Dance', width=15,height=3,bd='10',command=dancetoggle)
dancebutton.place(x=40,y=220)
      
 
# variables to define the center of the canvas
global cx, cy
cx = 180/2
cy = 200/2
       
#create the canvas
global Lfarm, Rtarm, Lfleg, Rtleg, part
msm = Canvas(mw,width=180,height=200, bg='yellow')
msm.place(x=10,y=25)

# Draw the figure and place it
head = msm.create_oval(cx-25,cy-75,cx+25,cy-25, fill='gray90')
body = msm.create_line(cx,cy-25,cx,cy+25,width = 3)
Lfarm = msm.create_line(cx,cy, cx-30,cy-20, width=2)
Rtarm = msm.create_line(cx,cy, cx+30,cy-20, width=2)
Lfleg = msm.create_line(cx,cy+25, cx-20,cy+75, width=2)
Rtleg = msm.create_line(cx,cy+25, cx+20,cy+75, width=2)
msm.pack() 

mw.mainloop()