def checkString(message):
    result = {'UPPER':0,'LOWER':0}
    for i in message:
        if i.isupper():
            result['UPPER']+=1
        elif i.islower():
            result['LOWER']+=1
    x = 'UPPER = '+str(result['UPPER'])+'\nLOWER = '+str(result['LOWER'])
    return x        
a = input('Input String : ')
print(checkString(a))