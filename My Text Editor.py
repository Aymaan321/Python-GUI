from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
# Setup root window

window = Tk()
window.title("Codingal's text editor")
window.geometry('600x700')

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

def open_file():
    file_path = askopenfilename(filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not file_path:
        return
    txt_edit.delete(1.0, END)
    with open(file_path, 'r') as input_file:
        text = input_file.read()
        txt_edit.insert(END, txt)
        input_file.close()
    window.title(f"Codingal's Text Editor-{file_path}")

def save_file():
    file_path = asksaveasfilename(defaultextension='txt', filetypes=[('Text Files', '*.txt'), ('All Files', '*.*')])
    if not file_path:
        return
    with open(file_path, 'w') as output_file:
        text = txt_edit.get(0.1, END)
        output_file.write(text)
    window.title(f"Codingal's Text Editor-{file_path}")

txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
button_open = Button(fr_buttons, text='Open', command=open_file)
button_save = Button(fr_buttons, text='Save As', command=save_file)

button_open.grid(row=0, column=0, sticky='ew', padx=5, pady=5)
button_save.grid(row=0, column=0, sticky='ew', padx=5)
fr_buttons.grid(row=0, column=0, sticky='ns')
txt_edit.grid(row=0, column=1, sticky='nsew')

window.mainloop()
