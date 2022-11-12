from tkinter import *
import speedtest 

def check_speed():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3))+" Mbps"
    up = str(round(sp.upload()/(10**6),3))+" Mbps"

    T_lab.config(text=down)
    TS_lab.config(text=up)

nt = Tk()
nt.geometry("550x700")
nt.title(" Internet Speed Test ")
nt.config(bg="Blue")


IS_lab = Label(nt,
            text="Internet Speed Test",
            font=("Time new Roman",30,"bold"),
            bg="Blue",
            fg="White"
            )
IS_lab.place(x=80,y=40,height=50,width=380)  

DS_lab = Label(nt,
            text="Download Speed",
            font=("Time new Roman",26,"bold"),
            bg="Blue",
            fg="White"
            )
DS_lab.place(x=80,y=140,height=50,width=380)

T_lab = Label(nt,
            text="00",
            font=("Time new Roman",26,"bold"),
            bg="Blue",
            fg="White"
            )
T_lab.place(x=80,y=210,height=50,width=380)

US_lab = Label(nt,
            text="Upload Speed",
            font=("Time new Roman",26,"bold"),
            bg="Blue",
            fg="White"
            )
US_lab.place(x=80,y=280,height=50,width=380)

TS_lab = Label(nt,
            text="00",
            font=("Time new Roman",26,"bold"),
            bg="Blue",
            fg="White"
            )
TS_lab.place(x=80,y=350,height=50,width=380)

cks_btn = Button(nt,
                text="Check Speed",
                font=("Time New Roman",35,"bold"), 
                relief=RAISED, 
                cursor="plus",
                command=check_speed)
cks_btn.place(x=80,y=450,height=50,width=380)
nt.mainloop()