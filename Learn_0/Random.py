import random
item = [1,2,3,4,5,'phol','saf']

for i in range(10):
    x = random.choice(item)
    

a1 = random.random() # random 0 - 1
a2 = random.uniform(100,120) # random x - y ทศนิยม
a3 = random.randrange(1,10) # สุ่มตัวเลข 1 ถึง 10  จำนวนเต็ม
a4 = random.randrange(1,10,2) # สุ่มตัวเลข 1 ถึง 10  จำนวนเต็ม เลขคี่ 
a5 = random.randint(1,5) # สุ่มตัวเลขจำนวนเต็ม
a6 = random.choice(item) #สุ่ม list

random.shuffle(item) #สุ่มสลับสมาชิกใน list (สามารถใส่ str ได้เลย)
x = random.choice('1234') #สุ่มสลับสมาชิกใน list (สามารถใส่ str ได้เลย)
print(random.sample(item,len(item)))
