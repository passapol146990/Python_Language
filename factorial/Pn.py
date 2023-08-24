import tkinter as tk

def factorial_loop():
    num1 = int(window_try.get())

    if num1 == 1:
        show1 = num1
        show_num.configure(text=show1)
    else:
        f = 1
        for i in range(1, num1+1):
            f = f * i
        show_num.configure(text=f, font=60)


#หน้าต่าง
window = tk.Tk()
window.title('fatorial number')
window.minsize(width=720, height=420)
#ตัวหนังสือ
lable_lable = tk.Label(master=window, text='กรอกเลขที่ต้องการหา Fatorial', font=30)
lable_lable.pack(pady=10)
#รับค่า
window_try = tk.Entry(master=window)
window_try.pack()
#ปุ่มแสดงผล
window_buuton = tk.Button(bg="black", fg="white", text='ok', width=13, master=window,
                          command=factorial_loop)
window_buuton.pack(pady=15)

show_num = tk.Label(master=window)
show_num.pack(pady=30)


window.mainloop()