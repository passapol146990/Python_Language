# คือการแปลงเป็น str + {}
a = 89
print(f'A is grad: {a}')
#ใส่คอม่า
b = 140_555_566
print(f'ใส่คอมม่า : {b:,d}')
print(f'{b:,}')
print(f'{b:,.2f}')
#ทศนิยม
c = 3.123456
print(f'c is : {c:.2f}')
#ช่องว่าง
a1 = '  hello world     '
print(a1.strip())

# ใส่เลข 0 ข้างหน้าตามที่ต้องการ
d,e = 4,500
print(f'd is : {d:03}',f'e is : {e:04}')

data = [
    {'id':1,'name':'a','salary':15000},
    {'id':2,'name':'b','salary':20000}
]
for i in data:
    print(f'{i["id"]:03} {i["name"]:3} {i["salary"]:,d}')