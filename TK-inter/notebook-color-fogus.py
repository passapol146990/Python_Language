from tkinter import *
from tkinter.ttk import Notebook, Style


ws = Tk()

Mysky = "#DCF0F2"
Myyellow = "#F2C84B"

style = Style()

style.theme_create( "dummy", parent="alt", settings={
        "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
        "TNotebook.Tab": {
            "configure": {"padding": [5, 1], "background": Mysky },
            "map":       {"background": [("selected", Myyellow)],
                          "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("dummy")

notebook = Notebook(ws)
frame1 = Frame(notebook, width=300, height=200)
notebook.add(frame1, text = 'First')
frame2 = Frame(notebook, width=300, height=200)
notebook.add(frame2, text = 'Second')
notebook.pack(expand=1, fill='both', padx=7, pady=7)

Button(ws, text='dummy!').pack(fill='x')

ws.mainloop()