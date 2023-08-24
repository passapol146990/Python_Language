import requests
from bs4 import BeautifulSoup

# กำหนด URL ของเว็บไซต์ที่ต้องการดึงข้อมูล
url = 'https://reg.msu.ac.th/registrar/class_info_1.asp?avs405488016=18&backto=enroll'

# ส่งคำขอ GET เพื่อดึงเนื้อหาของหน้าเว็บ
response = requests.get(url)
# print(response)
# สร้างตัวแปรเพื่อเก็บเนื้อหา HTML ของหน้าเว็บ
html_content = response.content
# print(html_content)
# ใช้ Beautiful Soup เพื่อแปลงเนื้อหา HTML เป็นโครงสร้างที่สามารถนำมาดึงข้อมูลได้
soup = BeautifulSoup(html_content, 'html.parser')
# print(soup)
# ใช้เมธอด find() หรือ find_all() ของ Beautiful Soup เพื่อค้นหาและดึงข้อมูลที่ต้องการจากตารางเรียน
# จากนั้นสามารถดำเนินการประมวลผลข้อมูลตามต้องการ

# ตัวอย่างการค้นหาและดึงข้อมูลตารางเรียนจากตารางที่มี id="timetable"
# timetable_table = soup.find('tr', {'class': 'normalDetail'}) เอามาแค่ไม่กี่อัน
timetable_table2 = soup.find_all('tr', {'class': 'normalDetail'}) #เอามาทั้งหมด
# gettd = timetable_table2.find_all('td', {'align': 'RIGHT'})
print('modsSubject: 0041001')
# print(gettd)
for element in timetable_table2:
    print(f':{element}\n')

# ตัวอย่างการวนลูปเพื่อดึงข้อมูลแต่ละแถวและคอลัมน์ในตาราง
rows = timetable_table2
# print(rows)
