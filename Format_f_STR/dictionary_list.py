languages = {"END":"ภาษาอังกฤษ","TH":"ภาษาไทย","JPY":"ภาษาญี่ปุ่น"}
languagesKeys = languages.keys()
languagesValues = languages.values()
print(list(languagesKeys))
print(list(languagesValues))

# สลับจาก key --> value
reverseDict = {value:key for key,value in languages.items()}
print(reverseDict)

# การรวม dictionary
g1 = {"A":80,"B":70,"C":60}
g2 = {"D":50,"F":40}
grad = {**g1,**g2}
print(grad)
# การรวม tuple จะใช้ * แค่ตัวเดียว

# การใส่ค่าข้อมูลเข้าใร func แบบไม่จำกัด
def calculate(**k):
    result = k['a'] + k['b']
    print(result)

calculate(a=5,b=5,c=20)


# lambda func
print((lambda x,y:x+y)(10,20))