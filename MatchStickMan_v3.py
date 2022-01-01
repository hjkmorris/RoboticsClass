# -*- coding: utf-8 -*-
"""
Created on Sun Dec 26 11:09:47 2021

This is an interactive form of the matchstick man code. Pressing the dance button turns on the music only. The user then uses the arrow keys to make the 
figuredance

@author: hjkmo
"""
import tkinter as tk
from tkinter import ttk
import time

from PIL import Image, ImageDraw
from matplotlib import animation

from playsound import playsound
from threading import Thread

class MainGUI:
    def __init__(self):
        #create the canvas
        self.root = tk.Tk()
        self.root.geometry('200x300')
        title = tk.Label(self.root, text="Dancing Figure",bg="green",font=("bold",10))
        title.pack()
        
        global msm
        msm=tk.Canvas(self.root,width=180,height=200, bg='yellow')
        msm.place(x=10,y=25)           
        
        # Add a button to the window
        global dancebutton, dancesw
        dancesw=False
        dancebutton = tk.Button(self.root,text='Dance', width=15,height=3,bd='10',command=self.dancetoggle)
        dancebutton.place(x=40,y=220)  
        
        # variables to define the center of the canvas       
        global cx, cy
        cx = 180/2
        cy = 200/2
        
        # Draw the figure and place it
        head = msm.create_oval(cx-25,cy-75,cx+25,cy-25, fill='gray90')
        body = msm.create_line(cx,cy-25,cx,cy+25,width = 3)
        Lfarm = msm.create_line(cx,cy, cx-30,cy-20, width=2)
        Rtarm = msm.create_line(cx,cy, cx+30,cy-20, width=2)
        Lfleg = msm.create_line(cx,cy+25, cx-20,cy+75, width=2)
        Rtleg = msm.create_line(cx,cy+25, cx+20,cy+75, width=2)
        
        # Bind canvas with key events
        msm.bind("<Up>", self.up)
        msm.bind("<Down>", self.down)
        msm.bind("<Left>", self.left)
        msm.bind("<Right>", self.right)
        msm.focus_set()   
        
        self.root.mainloop() # Create an event loop
        
    def dancetoggle(self):
        global dancesw
        
        if dancesw: #if already paused
            dancesw=False #resume
            dancebutton['text'] = 'Dance'
        else: #if not paused
            dancesw=True
            dancebutton['text'] = 'Stop Dancing'
            thread = Thread(target=play_sound, daemon = True)
            thread.start() 
            
    def left(self,event):   
        #Move the left arm
        print("Left arrow pressed.")
        newpart = msm.create_line(cx,cy, cx-30,cy-20, width=2)
        self.root.update()
        #delmsm(newpart)
    
    def right(self,event):   
        #Move the right arm
        print("Right arrow pressed.")
        newpart = msm.create_line(cx,cy, cx+30,cy-20, width=2)
        self.root.update()
        #delmsm(newpart)
        
    def up(self,event):     
        #Move the right leg
        print("Up arrow pressed.")
        newpart = msm.create_line(cx,cy+25, cx+30,cy+75, width=2)
        self.root.update()
        #delmsm(newpart)
            
    def down(self,event):   
        #Move the left leg
        print("Down arrow pressed.")
        newpart = msm.create_line(cx,cy+25, cx-30,cy+75, width=2)
        self.root.update()
        #delmsm(newpart)     
                
def play_sound():
    playsound('Ironic.mp3')
    
def move_part(part, x, y):   
    part = msm.create_line(cx,cy, cx+30+x,cy-20+y, width=2)
    
def delmsm(part):
    msm.delete(part) 
    

MainGUI()
