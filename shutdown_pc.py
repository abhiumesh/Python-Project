from tkinter import *
import os

window = Tk()
window.title("ShutDown PC")
window.geometry("500x500")
window.config(bg="Blue")

def restart():
    os.system("shutdown /r /t 1")

def restart_time():
    os.system("shutdown /r /t 20")

def logout():
    os.system("shutdown -l")

def shutdown():
    os.system("shutdown /s /t 1")

r_btn = Button(window, 
            text = "Restart",  
            font=("Time New Roman",26,"bold"), 
            relief=RAISED, 
            cursor="plus",
            command=restart)
r_btn.place(x=150,y=80,height=40,width=200)

rt_btn = Button(window, 
            text = "Restart Time",  
            font=("Time New Roman",15,"bold"), 
            relief=RAISED, 
            cursor="plus",
            command=restart_time)
rt_btn.place(x=150,y=150,height=40,width=200)

lg_btn = Button(window, 
            text = "LogOut",  
            font=("Time New Roman",15,"bold"), 
            relief=RAISED, 
            cursor="plus",
            command=logout)
lg_btn.place(x=150,y=230,height=40,width=200)

st_btn = Button(window, 
            text = "ShutDown",  
            font=("Time New Roman",15,"bold"), 
            relief=RAISED, 
            cursor="plus",
            command=shutdown)
st_btn.place(x=150,y=310,height=40,width=200)

window.mainloop()