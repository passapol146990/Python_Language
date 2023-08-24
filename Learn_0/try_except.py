def inputName():
    try:
        name = str(input('name : '))
        if name == 'phol':
            raise Exception('The system has this name now!')
        num1 = int(input('number 1 :'))
        num2 = int(input('number 2 :'))
        if num1 == 0 or num2 == 0:
            return
        if num1 < 0 or num2 < 0:
            raise Exception('Do not enter the number 0!')
        print('name is : '+name)
    except ValueError as e:
        print(e)
        
inputName()