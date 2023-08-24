import tkinter as tk

def factorial2():
    num1 = int(window_try.get())
    num2 = int(window_try2.get())
    sol1 = int(num1-num2)
    if sol1 == 1:
        show_num.configure(text=1)
    else:
        g = 1
        for u in range(1, sol1+1):
            g = g * u
        #แสดงผล
        n = str(num1)
        s = str(num2)
        solshow = 'P' + n + ',' + s
        show_num.configure(text=g)
        show_sol.configure(text=solshow)

#หน้าต่าง
window = tk.Tk()
window.title('fatorial number')
window.minsize(width=720, height=420)
#ตัวหนังสือ
lable_lable = tk.Label(master=window, text='กรอกเลขที่ต้องการหา Fatorial', font=30)
lable_lable.pack(pady=10)
lable_lable2 = tk.Label(master=window, text='Pn,r')
lable_lable2.pack()
#จี้แจง n,r
lable_lablen = tk.Label(master=window, text='ใส่ n')
lable_labler = tk.Label(master=window, text='ใส่ r')

#รับค่า
lable_lablen.pack()
window_try = tk.Entry(master=window)
window_try.pack(pady=10)

lable_labler.pack()
window_try2 = tk.Entry(master=window)
window_try2.pack()

#ปุ่มแสดงผล
window_buuton = tk.Button(bg="black", fg="white", text='ok', width=13, master=window,
                          command=factorial2)
window_buuton.pack(pady=15)
#แสดงผลออก
show_sol = tk.Label(master=window, font=5)
show_sol.pack()
show_num = tk.Label(master=window, font=60)
show_num.pack(pady=30)


window.mainloop()