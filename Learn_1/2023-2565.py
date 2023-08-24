y1 = str(input('input Year:')) # ใส่ปี ค.ศ.
y2 = str(int(y1)+543) # แปลงเป็นปี พ.ศ.
sum1 ,sum2 = [int(i) for i in y1],[int(i) for i in y2]

print('พ.ศ.',y2)
print('นำตัวเลขปี ค.ศ. มาบวกกันได้ :',sum(sum1))
print('นำตัวเลขปี พ.ศ. มาบวกกันได้ :',sum(sum2))