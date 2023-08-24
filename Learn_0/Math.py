import math
a1 = math.sqrt(64) #สแควรูท
a2 = math.floor(80.4) #ปัดเศษลง
a3 = math.ceil(80.4) #ปัดเศษขึ้น
pi = math.pi #ค่าพาย

#ตรีโกณมิติ sin cos tan
sin = math.radians(30) # แปลง ดีกรี เป็น radians
sin1 = math.sin(sin) # แปลง radians เป็นค่า มุมตรีโกณมิติ 
cos = math.radians(90)
cos1 = math.cos(cos) #  
tan = math.radians(30)
tan1 = math.tan(tan) # 

# คำนวณระยะห่างระหว่างกราฟ
point1 = [5,4]
point2 = [5,13]
d = math.dist(point1,point2)

# ลอการึทึม
l1 = math.log10(1000)  # หาค่า ลอการึทึม 10*10*10 = 1000
l2 = math.log2(32) # หาค่า ลอการึทีม 2*2*2*2*2 = 32

print(l1,l2)