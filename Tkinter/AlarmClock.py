from time import strftime 
from tkinter import * 

import time
import datetime
from pygame import mixer
 
root = Tk() 
root.title('Alarm Clock')
root.iconbitmap('./Tkinter/Phoenix.ico')
root.config(padx=6, pady=6)

def setalarm():
    alarmtime=f"{hrs.get()}:{mins.get()}:{secs.get()}"
    print(alarmtime)
    if(alarmtime!="::"):
        alarmclock(alarmtime) 

def alarmclock(alarmtime): 
    while True:
        time.sleep(1)
        time_now=datetime.datetime.now().strftime("%H:%M:%S")
        print(time_now)
        if time_now==alarmtime:
            Wakeup=Label(root, font = ('arial', 20, 'bold'),
            text="Wake up!Wake up!Wake up",bg="DodgerBlue2",fg="white").grid(row=6,columnspan=3)
            print("wake up!")
            mixer.init()
            mixer.music.load(r'file_goes_here')
            mixer.music.play()
            break


hrs=StringVar()
mins=StringVar()
secs=StringVar()

greet=Label(root, font = ('Consolas', 20, 'bold'),
text="Take a short nap!").grid(row=1,columnspan=3,padx=4, pady=4)

hrbtn=Entry(root,textvariable=hrs,width=5,font =('arial', 20, 'bold'))
hrbtn.grid(row=2,column=1, padx=4, pady=4)

minbtn=Entry(root,textvariable=mins,
width=5,font = ('arial', 20, 'bold')).grid(row=2,column=2, padx=4, pady=4)

secbtn=Entry(root,textvariable=secs,
width=5,font = ('arial', 20, 'bold')).grid(row=2,column=3, padx=4, pady=4)

setbtn=Button(root,text="set alarm",command=setalarm,bg="DodgerBlue2",
fg="white",font = ('arial', 20, 'bold')).grid(row=4,columnspan=3, padx=4, pady=4)

timeleft = Label(root,font=('arial', 20, 'bold')) 
timeleft.grid(padx=4, pady=4)
  
mainloop() 