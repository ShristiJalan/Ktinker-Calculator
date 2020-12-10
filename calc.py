import tkinter as tk
import tkinter.ttk as ttk

win = tk.Tk()

win.title("Calculator")

# win.configure(width=300,height=300,background='skyblue')

win.geometry('300x300+200+200')

label = ttk.Label(win,text="Hello World")
label.pack()
button = ttk.Button(win,text="Hello")

button.pack()
label.pack()

win.mainloop()

   