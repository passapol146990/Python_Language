# fw = open('code.txt','a',encoding='utf-8')
# for i in range(1,15):
#     x = '00'+str(45000+i)+'\n'
#     fw.writelines(x)

fr = open('code.txt','r',encoding='utf-8')
fd = fr.readlines()
for i in fd:
    try:
        print(int(i))
    except:
        pass
