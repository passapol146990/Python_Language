from tkinter import *
from tkinter.ttk import Notebook, Style

x = 10
y = 100


ws= Tk()
style = Style()
style.theme_create( "MyStyle", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {"configure": {"padding": [y, x] },}})

style.theme_use("MyStyle")

notebook = Notebook(ws, width=250, height=250)
tab1 = Frame(notebook)
notebook.add(tab1, text = 'Welcome to tab one')
tab2 = Frame(notebook)
notebook.add(tab2, text = 'Welcome to tab two')
notebook.pack(expand=True, fill=BOTH)

Button(ws, text='Some Text!').pack(fill=X)

ws.mainloop()