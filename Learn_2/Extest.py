import tkinter as tk
def replyname():
    name1 = input_name.get()
    replyhello.configure(text="hello "+name1)
    return

window = tk.Tk()
window.title("PHOL APP")
window.minsize(width=400, height=400)

title_laber = tk.Label(text="hello, what you name?")
title_laber.pack()

input_name = tk.Entry()
input_name.pack()


ok_name = tk.Button(text="ok", command=replyname)
ok_name.pack()

replyhello = tk.Label(width=20, height=20)
replyhello.pack()

window.mainloop()