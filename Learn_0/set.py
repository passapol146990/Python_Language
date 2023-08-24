a1 = {'a1', 'a2', 'a3'}
a2 = {'a2', 'a3', 'a4'}
# สมาชิกทั้งหดม
a1 = a1.union(a2)
print(a1)

a1 = {'a1', 'a2', 'a3'}
a2 = {'a2', 'a3', 'a4'}
# สมาชิกที่ไม่ซ้ำกัน
a1 = a1.difference(a2)#สมาชิกใน a1 ที่ไม่ซ้ำกับ a2
print(a1)

a1 = {'a1', 'a2', 'a3'}
a2 = {'a2', 'a3', 'a4'}
#สมาชิกที่ซ้ำกัน
a1 = a1.intersection(a2)
a2 = a2.intersection(a1)
print(a1,a2)