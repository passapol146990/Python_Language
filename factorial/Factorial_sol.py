def factorial(x):
    return (x == 1) and x or (x != 1) and x*factorial(x-1)

def factorial_l(x):
    if(x == 1):
        return x
    else:
        return x * factorial_l(x-1)

sum = 1
for i in range(5,1,-1):
    sum = sum * i

print(factorial(5))
print(factorial_l(5))
print(sum)