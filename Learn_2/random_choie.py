import random
def factorial(x):
    return (x == 1) and x or (x != 1) and (x*factorial(x-1))

def to_set2(x):
    a,a1 = [],set(x)
    for i in list(a1):
        a.append(x.count(i)) #เอาผลรวมจำนวนที่หาได้ไปไว้ที่ a
    c = 0
    for i in a:
        if i != 1:
            c += i
    if c == 0:
        c = 1
    return factorial(len(x))//factorial(c)

def run1():
    a,b = [],[]
    loop = int(input("จำนวนเลข :"))
    for i in range(loop):
        a.append(int(input()))
    c = to_set2(a)
    while len(b) != c:
        if len(a) <= 1:
            b.append(a)
            break
        a1 = random.sample(a,len(a))
        if a1 not in b:
            b.append(a1)
    b.sort()
    for i in b:
        print(i)
    print(len(b))

run1()