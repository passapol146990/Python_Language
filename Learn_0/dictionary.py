color = {'red':'แดง','green':'เขียว','blue':'น้ำเงิน',15:'บึงไฮ'}
pets = dict(cat='แมว',dog='หมา',chicken='ไก่')
print(pets['cat'],color[15])

for v,k in color.items():
    print(v,k)
for items in color.values():
    print(items)
#.pop('red') ลบสีแดงออก
#.popitem() เอาตัวที่อยู่หลังเพื่อนออก
# .clear() ล้างข้อมูลออก

data = {
    "แม่เอี้ยง":{
        'name':'แม่เอี้ยง',
        'menus':['ชาไทย','น้ำส้ม'],
        'zone':'บึงไฮ'
    },
    "พัสพล":{
        'name':'พัสพล',
        'menus':['ขนม','นม'],
        'zone':'บึงไฮ'
    },
    "ปังปอน":{
        'name':'เจน',
        'menus':['ต้มยำกุ้ง','ผัดไทย'],
        'zone':'กมลาไสย'
    }
}
print(data['พัสพล']['menus'])