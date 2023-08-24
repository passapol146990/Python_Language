import tkinter as tk

def show_output():
    number = int(number_input.get())
    if number == 0:
        output_lable.configure(text='erre')
        return

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_lable.configure(text=output)

window = tk.Tk()
window.title('JustPython')
window.minsize(width=400, height=400)

title_lable = tk.Label(master=window, text='สูตรคูณแม่', font=30)
title_lable.pack(pady=20)

number_input = tk.Entry(master=window, width=20)
number_input.pack()

go_button = tk.Button(master=window, text='ได้แก่', command=show_output, width=10, height=2)
go_button.pack()

output_lable = tk.Label(master=window)
output_lable.pack(pady=20)

window.mainloop()