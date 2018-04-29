from tkinter import *

def update_time():
    if(running):
        global time
        time[2]+=1
        if(time[2]>=60):
            time[2]=0
            time[1]+=1
        if(time[1]>=60):
            time[1]=0
            time[0]+=1
        tempTime = str(time[0])+" : "+str(time[1])+" : "+str(time[2])
        timeText.configure(text=tempTime)
    root.after(10, update_time)

def start():
    global running
    running = True


def pause():
    global running
    running = False
   

master = Tk()
timeText = Label(master, text="00 : 00 : 00",relief=RAISED)
timeText.pack()

running = False
time = [0,0,0]

startbutton = Button(root, text="Start", command = start)
startbutton.pack(side="left")

#resetbutton = Button(master, text="Reset", command = reset)
#resetbutton.pack(side="left")

pausebutton = Button(root, text="Pause", command = pause)
pausebutton.pack(side="left")

#stopbutton = Button(root, text="Stop", command = stop)
#stopbutton.pack(side="left")

update_time()
root.mainloop()


