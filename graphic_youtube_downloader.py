# add library
import pytube
import os
from tkinter import *
from tkinter import messagebox

# creat base of gui
win = Tk()
win.title("GRAPHIC YOUTUBE DOWNLOADER")
win.maxsize(400,400)
win.minsize(400,400)
win.config(bg="yellow")

global entry_value 
entry_value = StringVar()
s = str(win.clipboard_get())

# function that download youtube
def doo():
	link = str(entry_value.get())
	if link == "":
		messagebox.showerror("showerror", "لینک را وارد کنید")
	pythub=pytube.YouTube(link)
	res=pythub.streams.first()
	res.download("DOWNLOAD.mp4")
	if "DOWNLOAD.mp4":
		messagebox.showeinfo("showeinfo", "دانلود انجام شد")

def copy(textt):
	entry_value.set(textt)
	return
	
# design by adding label and button
global en1 
en1 = Entry(win,bg="brown",textvariable=entry_value ,fg="beige",font=('B nazanin',15)).place(x=30,y=130,height=40,width=280) 
b1 = Button(win,text="دانلود",fg="green",bg="purple",height=0,width=5,font=('B titr' , 20),command=doo).place(x=110,y=220)
b2 = Button(win,text="پیست",fg="green",bg="purple",height=-2,width=4,font=('B titr' , 15),command=lambda:copy(s)).place(x=318,y=120)
l2 = Label(win,text="لطفا لینک مورد نظر را وارد کنید" , fg="black",bg="yellow", font=('B titr',16)).place(x=50,y=50)

# run gui
win.mainloop()
