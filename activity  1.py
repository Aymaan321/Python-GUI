from tkinter import *

window = Tk()
window.title('Event Handler')
window.geometry('100x100')

def handle_press(event):
    print(event.char)

window.bind("<Key>", handle_press)

def event_click(event):
    print("The button was clicked")

button = Button(text='Click Me!')
button.pack()
button.bind("<Button-1>", event_click)

window.mainloop()
