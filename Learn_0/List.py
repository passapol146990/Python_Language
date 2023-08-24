# เพิ่มข้อมูลไปต่อหลัง
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# แทรกข้อมูลตรง idx
thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "orange")
print(thislist)

# เอา List ไปต่อท้าย List
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist)
