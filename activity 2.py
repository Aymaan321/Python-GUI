# write a program to create a pygame window that takes the user's name as input and displays the personalized message
# use button, labels, entry and text widgets to develop this application
from tkinter import *
from datetime import date
# create window
root = Tk()
root.title("Getting starrted with widgets")
root.geometry("400x300")
# add widgets and add label
lb1 = Label(text="Hey there!", fg="white", bg="#072F5F", height=1, width=300)
name_lb1 = Label(text="Full Name", bg="#3285F3")
name_entry = Entry()


def display():
    global message
    name = name_entry.get()
    message = " welcome to the application \nToday's date is "
    greet = "hello, " + name
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())


text_box = Text(height=3)
btn = Button(text="Begin", command=display, height=1, bg="#1261A0")
lb1.pack()
name_lb1.pack()
name_entry.pack()
text_box.pack()
btn.pack()

root.mainloop()
