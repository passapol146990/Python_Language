data = {'191':'เหตุด่วน','1669':'โรงพยาบาล','119':'ดับเพลิง'}

def searchNumber(message):
    for key,value in data.items():
        if value == message:
            print('เบอร์ติดต่อ : ',key)

searchNumber('ดับเพลิง')