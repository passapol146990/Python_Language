fw=open('score.txt','w',encoding='utf-8')
# เขียนแบบเว้นบรรทัด
fw.write('พัสพล สุทาธรรม')
# เขียนแบบไม่เว้นบรรทัด
fw.writelines('ขึ้นบรรทัดใหม่')
# ปิดการเขียนตลอด
fw.close()