from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import bs4
import time
import pandas as pd

def create_Excel(datax,name):
        df = pd.DataFrame(datax)
        df.to_excel('วิชาทั้งหมด.xlsx',sheet_name=name)

def read_table(table):
    # x = soup.find_all('tr',{'valign':'TOP'})[table]
    x = table

    passsub = ''
    professor = ''
    about = {1 : '',2 : '',3 : '',4 : ''}

    # อ่านเวลา สถาที่ สอบกลาง-ปลาย รวม demo[4]
    datatime = x.find_all('td')[4].text + ' '
    tit,settit = '', []
    for i in datatime:
        if(i != ' '):
            tit+=i
        else:
            if len(tit)>0:
                settit.append(tit)
            tit = ''

    mid,fil,title1 = False,False,''
    for i in range(len(settit)):
        if i == 0:about[1]= ''.join(settit[i])
        elif i == 1:about[2]= ''.join(settit[i])
        elif settit[i] == 'สอบกลางภาค':
            mid = True
            fil = False
            title1 = ''
        elif settit[i] == 'สอบปลายภาค':
            mid = False
            fil = True
            title1 = ''

        if mid:
            title1 += settit[i]
            if len(title1) >= 35:
                about[3] = title1
        else:
            title1 += settit[i]
            if len(title1) >= 35:
                about[4] = title1

    passsub = x.find_all('td')[1].text
    professor = x.find_all('td')[2].text
    # ไม่เอาพวกที่มีวงเล็บ
    # if '(' not in professor:
    if True:
        sumdata = {
            'passsub': passsub,
            'professor':professor,
            'timeLearn':about[1],
            'atLearn':about[2],
            'midLearn': about[3],
            'filLearn':about[4],
            'sec':x.find_all("td")[5].text,
            'numin':x.find_all("td")[6].text,
            'numemptry':x.find_all("td")[8].text
        }
        return sumdata

def create_Chrome():
    # 1 open google
    driver = webdriver.Chrome()
    url = str('https://reg.msu.ac.th/registrar/home.asp')
    driver.get(url)
    time.sleep(0.5)
    # 2 get 1
    try:
        close1 = driver.find_element(By.XPATH,'//*[@id="fancybox-close"]')
        close1.click()
        login = driver.find_element(By.XPATH,'//*[@id="menutive"]/a[3]')
        login.click()
        inputuser = driver.find_element(By.XPATH,'//*[@id="ASPxRoundPanel1_RPC"]/table/tbody/tr[1]/td[5]/input')
        inputpassword = driver.find_element(By.XPATH,'//*[@id="ASPxRoundPanel1_RPC"]/table/tbody/tr[2]/td[2]/input[1]')
        inputsubmit = driver.find_element(By.XPATH,'//*[@id="ASPxRoundPanel1_RPC"]/table/tbody/tr[3]/td[2]/font/input')
        inputuser.send_keys(66011212067)
        inputpassword.send_keys('146990aA')
        inputsubmit.submit()
        # search_code = driver.find_element(By.XPATH,'//*[@id="menutive"]/a[7]')
        # search_code.click()
    except ValueError:
        print(ValueError)
    time.sleep(0.5)
    try:
        close2 = driver.find_element(By.XPATH,'//*[@id="fancybox-close"]')
        close2.click()
        time.sleep(0.5)
    except:
        pass
    # 3 login
    for i in range(1,10):
        element = "//*[@id='menutive']/a["+str(i)+"]"
        searchsub = driver.find_element(By.XPATH,element)
        if searchsub.text == "ค้นหารายวิชา":
            searchsub.click()
            break
    time.sleep(0.5)
    return driver 


def AIP_GetSubject(SubCode,driver):
    # 4 get subject
    input = driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[2]/div/table[2]/tbody/tr[7]/td[2]/table/tbody/tr/td[4]/input[1]')
    keysub = SubCode
    input.send_keys(keysub+Keys.ENTER)
    time.sleep(0.5)
    # 5 เข้าถึงข้อมูลหน้าเว็บ
    data = driver.page_source # เข้าถึง html
    soup = bs4.BeautifulSoup(data)
    lentd = soup.find_all('tr',{'valign':'TOP'})
    time.sleep(0.5)
    # 6 read_table and create Excel
    result = {
            'รหัสวิชา':[],
            'วิชาและอาจารย์':[],
            'เวลาเรียน':[],
            'ที่เรียน':[],
            'สอบกลางภาค':[],
            'สอบปลายภาค':[],
            'sec':[],
            'จำนวนที่รับ':[],
            'จำนวนที่เหลือ':[]
    }
    try:
        for i in range(len(lentd)-1):
            re = read_table(soup.find_all('tr',{'valign':'TOP'})[i])
            sec = int(re['sec'])
            if (i+1) == (sec):
                # print(re['sec'],(i+1))
                result['รหัสวิชา'].append(str(re['passsub']))
                result['sec'].append(sec)
                result['วิชาและอาจารย์'].append(re['professor'])
                result['เวลาเรียน'].append(re['timeLearn'])
                result['ที่เรียน'].append(re['atLearn'])
                result['สอบกลางภาค'].append(re['midLearn'])
                result['สอบปลายภาค'].append(re['filLearn'])
                result['จำนวนที่รับ'].append(re['numin'])
                result['จำนวนที่เหลือ'].append(re['numemptry'])
            else:break
    except ValueError:
        print(ValueError)
    # print(result)

    # try:
    #     create_Excel(result)
    #     print(f'รหัส {SubCode} สำรเร็จ')
    # except ValueError:
    #     print(ValueError)
    # time.sleep(0.5)

    back = driver.find_element(By.XPATH,'//*[@id="menutive"]/a[2]')
    back.click()
    return result
    # driver.close()


driver = create_Chrome()
code = ['0041001','0041022','']
# API_GetSubject(code[0],driver)
with pd.ExcelWriter('วิชาทั้งหมด.xlsx',engine='xlsxwriter') as writer:
    for i in code:
        # data = API_GetSubject(i,driver)
        data = AIP_GetSubject(i,driver)
        df = pd.DataFrame(data)
        df.to_excel(writer,index=False,sheet_name=i)
print(f'สร้างชุดข้อมูลเสร็จเรียบร้อย')