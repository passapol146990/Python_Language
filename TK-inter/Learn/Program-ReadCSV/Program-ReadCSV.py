from tkinter import*
from tkinter import ttk
from tkinter import messagebox

font1 = ('Angsana New',25)
font2 = ('Angsana New',20)

##############  save to CSV ################
def load():
    # clear table
    table.delete(*table.get_children())
    # update table
    x1,x2 = read()
    i = 1 
    for x,y in zip(x1,x2):
        table.insert('','end',values=(i,x,y))
        i += 1

def save_to_csv():
    vocab = e1.get()
    meaning = e2.get()
    if len(vocab) > 0 and len(meaning) > 0:
        x1,x2 = read()
        if vocab not in x1 and meaning not in x2: 
            rd = open('./data.csv','a',encoding='utf8')
            rd.write(vocab+'1'+meaning+'2')

            v_vocab.set('') # clear
            v_meaning.set('') # clear
            e1.focus() # focus
    else:
        messagebox.showinfo('not data','don have data')

def edit_to_cvs():
    vocab = et1.get()
    meaning = et2.get()
    x1,x2 = read()

    new_d1, new_d2 = x1, x2 
    if len(vocab) > 0 and len(meaning) > 0:
        if vocab in x1:
            for i in range(len(x1)):
                if vocab == x1[i]:
                    new_d1[i] = vocab
                    new_d2[i] = meaning
        else:
            messagebox.showinfo('not data','is now data not in datas')

    else:
        messagebox.showinfo('not data','don have data')
    

    # write  new  data
    data = ''
    for x,y in zip(x1,x2):
        data = data + f'{x}1{y}2'      
    fw = open('data.csv','w',encoding='utf-8')
    fw.write(data)


def read():
    rd = open('data.csv', 'r',encoding='utf-8')
    l1 = rd.readlines()
    a, b, b1, c,c2 = [], '','',[],[]
    # เอาข้อมูลรายตัวมาใส่ใน 
    for i in l1:
        if i != '':
            a.append(list(i))
    # เอาข้อมูลใน a[][] มาจัดแบบข้อมูลให้เป็นชุดคำเดียวกัน
    for i in range(len(a)): 
        for u in a[i]:
                b += u
    for i in b:
        if i == '1':
            c.append(b1)
            b1 = ''
        elif i == '2':
            c2.append(b1)
            b1 = ''
        else:
            b1 += i
    return c,c2


############## windown ######################
gui = Tk()
# 400x400 ขนาดหน้าจอ +500+150 ตำแน่งโปรแกรม x, y
# gui.geometry('400x600+500+150') 
gui.minsize(width=400,height=500)
gui.title('โปรแกรมบันทึกคำศัพท์')

############### Notbook #####################
# สร้างแทบด้านบน t1 -t3 เป็น gui ได้เลย
tab = ttk.Notebook(gui)

t1 = Frame(tab)
t2 = Frame(tab)
t3 = Frame(tab)

tab.pack(fill=BOTH,expand=1)

tab.add(t1,text='Add data')
tab.add(t2,text='View data')
tab.add(t3,text='Edit data')


##############  หน้า1 ################
label1 = ttk.Label(t1,text='คำศัพท์',font=font1)
label1.pack()

# inout1
v_vocab = StringVar()
e1 = ttk.Entry(t1, textvariable=v_vocab, font=font2, width=30)
e1.pack()

# text2
label1 = ttk.Label(t1,text='ความหมาย',font=font1)
label1.pack()

# inout2
v_meaning = StringVar()
e2 = ttk.Entry(t1, textvariable=v_meaning, font=font2, width=30)
e2.pack()

# btn1
b1 = ttk.Button(t1,text='Save',command=save_to_csv)
b1.pack(ipadx=20,ipady=10,pady=20)




##############  หน้า2 ################
b2 = ttk.Button(t2,text='load',command=load)
b2.pack(ipadx=20,ipady=5,pady=2)

header = ['ID','Vocab','Meaning']
hdsize = [50,150,150]

table = ttk.Treeview(t2,columns=header,show='headings',height=20)
table.place(x=20,y=40)

# header
for h,s in zip(header,hdsize):
    table.heading(h,text=h)
    table.column(h,width=s)

# showdata 
x1,x2 = read()
i = 1 
for x,y in zip(x1,x2):
    table.insert('','end',values=(i,x,y))
    i += 1



##############  หน้า3 ################
label0 = ttk.Label(t3,text='แก้ไขคำศัพท์',font=font1)
label0.pack()

label1 = ttk.Label(t3,text='คำศัพท์',font=font2)
label1.pack()

# inout1
v_vocab = StringVar()
et1 = ttk.Entry(t3, textvariable=v_vocab, font=font2, width=30)
et1.pack()

# text2
label1 = ttk.Label(t3,text='ความหมาย',font=font2)
label1.pack()

# inout2
v_meaning = StringVar()
et2 = ttk.Entry(t3, textvariable=v_meaning, font=font2, width=30)
et2.pack()

# btn1
b1 = ttk.Button(t3,text='Save',command=edit_to_cvs)
b1.pack(ipadx=20,ipady=10,pady=20)


gui.mainloop()