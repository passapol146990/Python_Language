import csv

def write_csv(datalist):
    with open('csv.csv', 'a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def read_csv():
    with open('csv.csv', 'r',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

f = read_csv() # เอาข้อมูลใส่ใน f
a = ['phol','6','4']

# เช็คว่าข้อมูลใหม่ ว่าซ้ำกันใน ข้อมูลเดิมหรือไม่ ถ้าซ้ำไม่ให้เพิ่มเข้าไป
if a not in f: 
    write_csv(a)

# ลูปแสดงข้อมูล
for i in read_csv():
    print(i)