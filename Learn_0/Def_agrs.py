"""
* ใส่เครื่องหมายนี้ คือ tuple
"""
def add(*item):
    sum=0
    for i in item:
        sum+=i
    print(sum)
add(10,20)