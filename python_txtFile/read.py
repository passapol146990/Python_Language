"""
x = open('ชื่อไฟล์','รูปแบบ/อ่าน(r),เขียน(w(เขียนและสร้าง),x(สร้างเปล่าๆ))',(a)เพิ่ม,'แบบภาษาเช่น ภาษาไทย utf-8')
"""
import os
def show():
    # โชว์ txt ทั้งหมด
    fr = open("student.txt",'r',encoding='utf-8')
    print(fr.read())
    fr.close()

def show_lines():
    # อ่านไฟล์ตามบรรทัด ยกเว้นบรรทัด 1
    fr = open("student.txt",'r',encoding='utf-8')
    line1 = fr.readline()#อ่านทีละตัว
    line2 = fr.readlines()#อ่านทีบรรทัด
    for i in line2:
        print(i)

def input_txtw():
    # เพิ่มtxt ลบอันเก่าออก
    fw = open('student.txt','w',encoding='utf-8')
    name = input('ลบและเขียนทับใหม่ :')
    fw.write(name)
    fw.close()

def input_txta():
    # เพิ่มtxtไม่เว้นบรรทัด
    name = input('input : ')
    fa=open('student.txt','a',encoding='utf-8')
    fa.write('\n'+name)
    fa.close()

def delete(name):
    # ลบไฟล์
    try:
        if os.path.exists(name):
            os.remove(name)
            print('ลบไฟล์เรียบร้อยแล้ว')
        else:
            print('ไม่พบไฟล์นี้')
    except Exception as e:
        print(e)

try:
    show()
    input_txta()
    show_lines()
    show()
    
except Exception as e:
    print(e)
