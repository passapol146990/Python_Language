"""
เมื่อ Y ที่แล้ว นาย A แก่กว่านาย B จำนวน M เท่า
และปัจบันนาย A แก่กว่านาย B จำนวน n ปี
จงหาอายุของนาย A และนาย B
"""
n = int(input())
m = int(input())
y = int(input())
b = (n-y+(m*y))//(m-1)
a = b+n
print(a)
print(b)