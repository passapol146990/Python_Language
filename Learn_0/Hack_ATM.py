import random
password = '146990aA'
result = ''

def random_hack(password1):
    password = password1
    result = ''
    while result != password:
        result = ''
        for i in range(len(password)):
            list_number = random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            result = ''.join(list_number)+str(result)
            print('SEARCH :',result)
    print(password,result)
def index_password(password1):
    password = [str(i) for i in password1]
    result = [str(i) for i in range(len(password1))]
    list_number = ''
    for i in range(len(password)):
        while result[i] != password[i]:
            list_number = random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
            print('SEARCH :',list_number)
            result[i] = list_number
        print(result[i],'=',password[i])
    p2 ,p1= '',''
    for i in range(len(password)):
        p1 += password[i]
        p2 += result[i]

    print(p1,':',p2)
        
# random_hack(password)
index_password(password)