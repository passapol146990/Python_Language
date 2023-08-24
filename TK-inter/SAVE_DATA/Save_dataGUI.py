from tkinter import *
from tkinter import ttk, Tk, StringVar
from tkinter import messagebox
from csv import *
import time;
import pandas as pd 
import csv
from datetime import datetime

#--------- Windows Size Gui -------------------
root = Tk()
root.title('Manatchai - Job Descripyion')
root.geometry("685x520+10+0")

global sno
sno = 1

#----- Define a topic on the report -------
my_H = ttk.LabelFrame(root, text='Report')
my_H.grid(row=0, column=0, padx=15, pady=15, ipadx=5 ,ipady=3)

#---- Create GUI Window with *Pandas*    
table_header=('Date','Time','Description')
table = ttk.Treeview(my_H,columns=table_header,show='headings')

for column in table_header:
    table.heading(column, text=column)
    table.pack(fill="both", expand=True)

#------------ Code save add data -------------
def writecsv(datalist): 
    with open('mydata.csv','a',encoding='utf-8',newline='') as file:
        Writer = csv.writer(file) #fw = file writer
        Writer.writerow(datalist) 


#------------ Create a new data file -------------
def Create_CSV (datalist): 
    with open('mydata.csv','w',encoding='utf-8',newline='') as file:
        Writer = csv.writer(file) #fw = file writer
        datalist = (["Date","Time","Description"])
        Writer.writerow(datalist) 
        messagebox.showinfo("Information","Create A New Data File successfully")


#------------- Code Add Record -------------
def add_record():
    with open("mydata.csv","a",encoding='utf-8',newline='') as file:
        Writer=writer(file)

        if (txtDate.get()!="" and txtTime.get()!="" and txtDes.get()!=""):
            global sno
            table.insert("", index="end", iid=sno, values=(txtDate.get(), txtTime.get(),txtDes.get()))
            sno += 1

            #t = datetime.now().strftime('%Y%m%d %H%M%S')
            data1 = v_txtDate.get() # Fetch data from v_data variable
            data2 = v_txtTime.get()  
            data3 = v_txtDes.get()   
            text = [data1,data2,data3]
                   
            writecsv(text) # Save Add data to csv file. 
            messagebox.showinfo("Information","Save data to successfully")
            #----- del txet box data ------------
            v_txtDate.set('')
            v_txtTime.set('')
            v_txtDes.set('')
        else:
            messagebox.showinfo("Message ","Please complete all fields.")
        file.close()
        read_data_pandas() #-- Add New Data --

#--------- Code Read data file from **Pandas***    
def read_data_pandas():
    #cols = ['Date','Time','Description']
    # df = pd.read_csv('D:\python101\mydata.csv',encoding='utf-8')
    df = pd.read_csv('mydata.csv',encoding='utf-8')
    #df = pd.read_csv('D:\python101\mydata.csv',encoding='utf-8',usecols=cols)
    
    #-- Code Delete the data in table --
    for i in table.get_children():
        table.delete(i)
                          
    # -- Code Read new data into the table --       
    for index, row in df.iterrows():
        table.insert("", index, text=index, values=(tuple(row)))
          
        
#-------- Code Select Record ----------

def select_record():
    txtDate.delete(0,END)
    txtTime.delete(0,END)
    txtDes.delete(0,END)
    selected=table.focus()
    values=table.item(selected,'values')
    messagebox.showinfo("Message ","Select the desired text row")
    txtDate.insert(0,values[0])
    txtTime.insert(0,values[1])
    txtDes.insert(0,values[2])
#--------- Code Update Record ----------
def update_record():
    if(txtDate.get()!="" and txtTime.get()!="" and txtDes.get()!=""):    
        no = table.focus()[0] # column id
        selected = table.focus() # Row id
        table.item(selected, values=(txtDate.get(), txtTime.get(), txtDes.get()))
        #----Delete text box data ------
        txtDate.delete(0,END) 
        txtTime.delete(0,END)
        txtDes.delete(0,END)
    else:
        messagebox.showinfo("Message","Modified row text was successfully saved.")

#----------- Code UpRow Record -----------
def up_record():
    rows = table.selection()    
    for row in rows:
        table.move(row, table.parent(row), table.index(row)-1)

#---------- Code UpDown Record -----------
def down_record():
    rows = table.selection()    
    for row in rows:
        table.move(row, table.parent(row), table.index(row)+1)

#-------- Code Remove One Record ---------
def remove_one():
        x = table.selection()[0]
        table.delete(x)

#------- Code Remove Mery Record ----------
def remove_many():
    x = table.selection()
    for record in x:
        table.delete(record)    

#------ Code Remove All Record ------------
def remove_all():
    for record in table.get_children():
        table.delete(record)    

#--------------- Add Data ------------------
'''
data=[
    ["16/03/2566", "11:20", "พบลูกค้าต่างจังหวัด"],
    ["17/03/2566", "08:55", "ประชุมฝ่ายการตลาด"],
    ["18/03/2566", "09:20", "ประชุมฝ่ายขาย"],
    ["18/03/2566", "12:10", "กินข้าวกับลูกค้า"],
    ["19/03/2566", "09:45", "ประชุมบริษัท"],
    ["20/03/2566", "11:51", "ไปต่างประเทศ"],
    ["21/03/2566", "13:25", "ประชุมงานวิชาการ"]
]

for datas in data:
    table.insert("",index="end",iid="", values=(datas[0], datas[1], datas[2]))
    
'''
table.pack()

my_H1 = ttk.LabelFrame(root, text='Input Data')
my_H1.grid(row=1, column=0, padx=10, pady=10,ipadx=5 ,ipady=3)

#------------ Head data field  --------------

n1 = Label(my_H1,bg='#b3ffb3', text=" Date")
n1.grid(row=1, column=0,)

il = Label(my_H1,bg='#b3ffb3', text=" Time")
il.grid(row=1, column=1)
 
tl = Label(my_H1,bg='#b3ffb3', text="Job Description")
tl.grid(row=1, column=2)


#--------------  Text Box -----------------

v_txtDate = StringVar() #-- ตัวแปลที่ใช้ใน GUI ---
v_txtTime = StringVar()
v_txtDes = StringVar()

txtDate = Entry(my_H1,width=15,textvariable=v_txtDate,font=('Angsana New',15))   
txtTime = Entry(my_H1,width=12,textvariable=v_txtTime,font=('Angsana New',15))
txtDes = Entry(my_H1,width=30,textvariable=v_txtDes,font=('Angsana New',15))

txtDate.grid(row=2, column=0, padx=10, pady=5 )
txtTime.grid(row=2, column=1, padx=10, pady=5)
txtDes.grid(row=2, column=2,padx=10, pady=5)

btnAdd = Button(my_H1, text="Add Record",bg='#b3ffb3',fg='#1a1aff',font=('Arial',10,'bold'),padx=5 ,pady=3, command=add_record)
btnAdd.grid(row=2, column=3, ipadx=10,ipady=3)

#--------------  Button Funtion -----------------

my_H2 = ttk.LabelFrame(root, text='Buttom Funtion')
my_H2.grid(row=3, column=0, padx=10, pady=10,ipadx=3 ,ipady=3)

btnSaveFile = Button(my_H2,bg='#ffb366',fg='#0000ff', text="Create New CSV File" , command=Create_CSV)
btnSaveFile.grid(row=3, column=3, ipadx=9, ipady=3)

btnSelect = Button(my_H2,bg='#ffd966',fg='#0000ff', text="Select Record", command=select_record)
btnSelect.grid(row=3, column=1,ipadx=27, ipady=3)

btnUpdate = Button(my_H2,bg='#99ff99',fg='#140033', text="Update Record", command=update_record)
btnUpdate.grid(row=3, column=2,ipadx=25, ipady=3)

btnExit = Button(my_H2,bg='#ff4d4d',fg='#0000ff', text="Exit",font=('Arial',12,'bold'), command=lambda: exit())
btnExit.grid(row=3, column=4,ipadx=30, ipady=1)

btnMoveup = Button(my_H2,bg='#66ffff',fg='#0000ff', text="Move Up Record", command=up_record)
btnMoveup.grid(row=3, column=0,ipadx=20, ipady=3)

btnMoveDown = Button(my_H2,bg='#ff99bb',fg='#0000ff', text="Move Down Record", command=down_record)
btnMoveDown.grid(row=4, column=0,ipadx=12, ipady=3)

btnRemoveOne = Button(my_H2,bg='#d9ff66',fg='#0000ff', text="Remove one Record", command=remove_one)
btnRemoveOne.grid(row=4, column=1,ipadx=10, ipady=3)

btnRemoveMany = Button(my_H2,bg='#66ffb3',fg='#0000ff', text="Remove Many Record", command=remove_many)
btnRemoveMany.grid(row=4, column=2,ipadx=5, ipady=3)

btnRemoveAll = Button(my_H2,bg='#d966ff',fg='#0000ff', text="Remove all Record", command=remove_all)
btnRemoveAll.grid(row=4, column=3,ipadx=13, ipady=3)
read_data_pandas()

root.mainloop
