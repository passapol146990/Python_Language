import matplotlib.pyplot as plt
num = (1,2,3,4,5,6)
name = ["python","vaja","html","c#","drat"]
score1 = [5,2,5,3,1]
score2 = [1,2,3,4,5]

# กราฟจด
def plotG():
    plt.plot(num)
    

# กราฟแท่ง    
def barG():
    plt.bar(score1, score2)
    

#กราฟวงกลม
def priG():
    plt.pie(score1)

# สร้างหน้าต่างเพิ่ม1อัน
def figure():
    plt.figure()

def class1():
    # กำหนดในบรรทัดเดียว
    a = plt.pie(score1,labels=name,autopct="%.2f%%")
    b = plt.bar(name,score1,width=0.5,color='b',edgecolor='black')

plt.pie(score1,labels=name,autopct="%.2f%%")
# กำหนดหัวข้อ
plt.title("name",color='r')
# กำหนดหัวข้อแต่ละแกน
plt.xlabel("Language")
plt.ylabel("Leval")

plt.show()