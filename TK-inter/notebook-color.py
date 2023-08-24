from tkinter import *
from tkinter.ttk import Notebook, Style


ws = Tk()


ws.geometry("700x350")

# Create an instance of ttk style
style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background="Red")
style.map("TNotebook", background= [("selected", "red")])

# Create a Notebook widget
note =Notebook(ws)

# Add a frame for adding a new tab
frame1= Frame(note, width= 400, height=180)

# Adding the Tab Name
note.add(frame1, text= 'Tkinter-1')
frame2 = Frame(note, width= 400, height=180)
note.add(frame2, text= "Tkinter-2")

note.pack(expand= True, fill=BOTH, padx= 5, pady=5)
ws.mainloop()
