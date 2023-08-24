import pyautogui as at,time
data = list([])
#แก้ไขข้อมูล
def Editdata():
    while True:
        print('ถ้าคุณแก้ข้อมูลเสร็จแล้วให้พิมพ์ ok')
        numindex = int(input('เลขข้างหน้าตัวที่ต้องการเปลี่ยน : '))
        newdata = str(input('ใส่ข้อมูลใหม่ : '))
    
        if(numindex == 'ok' or newdata == 'ok'):
            showdata()
        else:
            data.insert(numindex, newdata)
            showdata()
#โชว์ข้อมูล
def showdata():
    for i in range(len(data)):
        print(str(i)+" "+data[i])
    meday = input('#######################\nถ้าต้องการเปลี่ยนข้อมูลให้พิมพ์ E ถ้าข้อมูลถูกต้องแล้วให้พิมพ์ Y :')
    if(meday == 'E'):
        print('Edit')
        Editdata()
    elif(meday == 'Y'):
        print('Yes')
        language = str(input('ถ้าข้อมูลของคุณเป็นภาษา ไทย ให้พิมพ์ thai\nถ้าข้อมูลของคุณเป็น อังกฤษ ให้พิมพ์ Eng : '))
        if(language == 'thai'):
            Search('thai')
        if(language == 'Eng'):
            Search(0)
        else:
            showdata()
#รับข้อมูล
def inputdata():
    nt = '####################################'
    print(nt+'\nข้อมูลตอนนี้:'+str(data)+"พิมพ์ 0 เพื่อสิ้นสุด\nในกรณีที่ท่านต้องการพิมพ์ภาษาไทย ให้ท่านพิมพ์เป็นภาษาอังกฤษทับตัวลงไปเลย\nอีกครั้ง!! พิมพ์เป็นภาษาอังกฤษเลย\n")
    while True:
        n = str(input(': '))
        if(n == '0'):
            break
        else:
            data.append(n)
    print('#######################\nเช็คข้อมูลของคุณ')
def Tolanguage(lng):
    eng1 =(1644,1079)
    eng2 = (1660,1044)
    thai =(1605,941)
    if(lng == 'thai'):
        at.click(eng1,duration=1)
        time.sleep(0.5)
        at.click(eng2,duration=0.5)
        at.click(thai,duration=0.5)
    else:
        pass
#Ai
def Search(R):
    time.sleep(0.3)
    at.press('win')
    time.sleep(0.5)
    at.write('excal')
    time.sleep(0.5)
    at.press('enter')
    time.sleep(1)

    Tolanguage(R)

    time.sleep(0.5)
    create = (352,279)
    collum1=(76,290)
    at.moveTo(create,duration=0.5)
    at.doubleClick(create)
    time.sleep(0.5)
    at.moveTo(collum1,duration=0.5)
    at.doubleClick(collum1)
    
    for j in range(len(data)):
        title = str(data[j])
        at.write(title)
        time.sleep(0.5)
        at.press('enter')
#หาตำแหน่งเม้า
def positionnow(num):
    time.sleep(num)
    print(at.position())
def run():
    inputdata()
    showdata()
    


