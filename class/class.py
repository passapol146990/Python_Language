class student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.score = 0
    def showdata(self):
        print(f'name : {self.name} ID : {self.id} score : {self.score}')
    def addscore(self,score):
        self.score += score

    #เวลานำไปใส่ใน list มันจะแสดงชื่อออกมาเลย จะไม่ error
    def __str__(self):
        return self.name
    #เช่นกันกับอันด้านบน 
    def __repr__(self) -> str:
        return self.name
    #บวกกัน ถ้านำคสาสบวกกันให้ทำฟังชันนี้
    def __add__(self,other):
        return self.score + other.score 
#สืบทอดสมบัติ
class address(student):
    def __init__(self,name,id,address):
        super().__init__(name,id)
        self.address = address
    def showdatasum(self):
        print(f'name : {self.name} ID : {self.id} score : {self.score} address : {self.address}')

st1 = address('phol',1,'KLS')
st1.addscore(10)
st2 = address('saf',2,'KLS')
st2.addscore(10)
print(st1+st2)