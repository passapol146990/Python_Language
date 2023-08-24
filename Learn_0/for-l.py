greeting = ['hi','hello','google bye']
people = ['phol','and','pop','saf']
result = [i+u for i in greeting for u in people]
print(result)

product = ['x1','x2','x3','x4','x5']
price = [10,20,30,40,50]
for x,y in zip(product[::-1],price):
    print(x,y)

title = ['axxa','aaa','aca','akaa','as']
titlea = []
for item in title:
    titlea.append(item.count('a'))
print(title)
print(titlea) 