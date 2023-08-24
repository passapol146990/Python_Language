account = {'นายA':0,'นายB':0}

def getBalance():
    print('ยอดเงินคงเหลือในบัญชี : ',account)

def deposit(money):
    print('ฝากเงินเข้าบัญชี A :',money)
    if not type(money) is int and not type(money) is float:
        raise Exception('ต้องป้อนตัวเลขเท่านั้น')
    if money < 0:
        raise Exception('ค่าตัวเลขต้องเป็นบวกเท่านั้น')
    account['นายA']+=money

def withdraw_transfer(money):
    print('ถอนเงินเข้าบัญชี B :',money)
    if not type(money) is int and not type(money) is float:
        raise Exception('ต้องป้อนตัวเลขเท่านั้น')
    if money < 0:
        raise Exception('ค่าตัวเลขต้องเป็นบวกเท่านั้น')
    if money > account['นายA']:
        raise Exception('ยอดเงินของท่านไม่เพียงพอ')
    account['นายB']+=money
    account['นายA']-=money


try:
    getBalance()
    deposit(500)
    getBalance()
    withdraw_transfer(501)
    getBalance()
except Exception as e:
    print(e)
