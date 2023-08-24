# fw = open('grad.txt','w',encoding='utf-8')
fa = open('grad.txt','a',encoding='utf-8')
fr = open('grad.txt','r',encoding='utf-8')
def input1():
    while True:
        ID = input("input ID s**:")
        if ID == 'exit':
            print('Exit now')
            break
        score = input("input score :")
        fa.writelines(ID[:3]+'\t'+score+'\n')
        # fa.close()

def cal_grad(a):
    grad_num = 'FFFFFDCBAAA'
    grad = (a < 0 or a > 100) and 'error' or grad_num[int(a)//10]
    return grad

def print_grad():
    for x in fr.readlines():
        ID = x[:3].strip()
        score1 = int(x[4:].strip())
        print('ID : ',ID,'score :',score1,'Grad :',cal_grad(score1))
input1()
print_grad()