import datetime as dt
result = dt.datetime.now()
def group1():
    print(result)
    print(result.strftime('%x')) # เดือน/วัน/ปี 
    print(result.strftime('%X')) # timeรวม
    print(result.strftime('%c')) #ชื่อวัน ชื่อเดือน เวลา ปี
    print(result.strftime('%p')) #Am Pm
    print(result.strftime('%H:%M:%S')) #time h:m:s
    print(result.strftime('%a:%B:%Y')) #dat วัน:เดือน:ปี 
    print(result.strftime('%d / %m / %Y')) #วัน/เดือน/ปี แบบตัวเลข

#หาลำดับ
def group2():
    print(result.strftime('%j')) #1-365 วันนี้อยู่ลำดับที่เท่าไหร่ของปี
    print(result.strftime('%w')) #หาลำดับวัน 0-6

#วัน
def group3():
    print(result.strftime('%d')) #วันที่
    print(result.strftime('%a')) #วันย่อ
    print(result.strftime('%A')) #วันเต็ม
    print(result.strftime('%b')) #เดือนชื่อย่อ
    print(result.strftime('%B')) #เดือนชื่อเต็ม
    print(result.strftime('%y')) #ปีย่อ
    print(result.strftime('%Y')) #ปีเต็ม

group1()
print(result.strftime('%Y%m%d %H:%M:%S')) 
