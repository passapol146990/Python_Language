num = []
while True:
    x = int(input())
    if(x<0):
        break
    num.append(x)
print(num)
num.sort()
print(num)
num.reverse()
print(num)