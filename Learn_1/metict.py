sum = []
m = int(input('input m:'))
n = int(input('input n:'))
"""
def input_oenlist(m,n):
    print('ใส่ตัวเลขที่ละตัว เรียงจากซ้ายไปขวา')
    #รับค่า ตัวเลขที่จะบวก
    for i in range(m*n):
        a1.append(int(input())) 
    for u in range(n*m):
        a2.append(int(input()))
"""
def input_threelist(m,n):
    x ,y = '',''
    #รับค่า ตัวเลขที่จะบวก
    for i in range(m):
        x = x+str(input())
    for u in range(n):
        y = y+str(input())
    return x , y
def input_list(*args):
    x1 = []
    for u in range(len(args)):
        for i in args[u]:
            if i == ' ':
                pass
            else:
                x1 += i
    return x1
x1 ,x2 = input_threelist(m,n)
a1 = input_list(x1)
a2 = input_list(x2)
#หาผลบวก
for x in range(m*n):
    num = int(a1[x])+int(a2[x])
    sum.append(num)
#แสดงผล
x ,y = [],0
print('\n')
for u in range(m):
    x ,l= [],''
    for i in range(n):
        x.append(int(sum[y]))
        y += 1
    for i in range(len(x)):
        l = l + str(x[i]) + ' '
    print(l)