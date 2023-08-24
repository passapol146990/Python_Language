def decimal_to_binary(decimal,base):
    base16 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    if decimal == 0:
        return '0'
    
    binary = ''
    print(f'{base}/{decimal}')
    while decimal > 0:
        mod = decimal % base
        if mod >= 10:mod = base16[mod]
        binary = str(mod) + binary
        decimal = decimal // base
        print(f'{base}/{decimal} = {mod}')
    
    return binary



# รับค่าจำนวนเต็มเป็นฐาน 10
decimal_number = int(input("กรุณาใส่เลขฐาน 10: "))
base = int(input("ฐานที่ต้องการ :"))
# เรียกใช้ฟังก์ชันแปลงฐาน 10 เป็นฐาน 2
binary_number = decimal_to_binary(decimal_number,base)

# แสดงผลลัพธ์
print(f'เลขฐาน {base} คือ:', binary_number)
