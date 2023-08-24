# import pandas as pd
# with pd.ExcelWriter('file1.xlsx') as writer:
#     writer.to_excel(writer,sheet_name='M1')
#     writer.to_excel(writer,sheet_name='M2')



import pandas as pd

# สร้าง DataFrame ตัวอย่าง
data = {'Column1': [1, 2, 3, 4],
        'Column2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)

# กำหนดชื่อไฟล์ .xlsx
file_name = 'ข้อมูล.xlsx'

# สร้าง sheet_name ใหม่อัตโนมัติ
existing_sheet_name = 'ชีทเดิม'
start_index = 1
num_sheets_to_add = 5  # จำนวนชีทที่ต้องการเพิ่ม

with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
    df.to_excel(writer, index=False, sheet_name=existing_sheet_name)

    for i in range(num_sheets_to_add):
        new_sheet_name = f'ชีทใหม่ {start_index + i}'
        df.to_excel(writer, index=False, sheet_name=new_sheet_name)

print(f'เพิ่มชีทใหม่ {num_sheets_to_add} ชีทเรียบร้อยแล้วในไฟล์ {file_name}')















# เพิ่มข้อมูลใหม่
import pandas as pd

# สร้าง DataFrame ตัวอย่าง
data = {'Column1': [1, 2, 3, 4],
        'Column2': ['A', 'B', 'C', 'D']}
df = pd.DataFrame(data)

# กำหนดชื่อไฟล์ .xlsx
file_name = 'ข้อมูล.xlsx'

# สร้าง sheet_name ใหม่อัตโนมัติ
existing_sheet_name = 'ชีทเดิม'
start_index = 1
num_sheets_to_add = 5  # จำนวนชีทที่ต้องการเพิ่ม

# สร้าง DataFrame ใหม่สำหรับแต่ละ sheet_name
data_new = {'Column3': [5, 6, 7, 8],
            'Column4': ['E', 'F', 'G', 'H']}
df_new = pd.DataFrame(data_new)

with pd.ExcelWriter(file_name, engine='xlsxwriter') as writer:
    # เขียน DataFrame เดิมลงในชีทเดิม
    df.to_excel(writer, index=False, sheet_name=existing_sheet_name)

    # เพิ่มข้อมูล DataFrame ใหม่ลงในแต่ละชีท
    for i in range(num_sheets_to_add):
        new_sheet_name = f'ชีทใหม่ {start_index + i}'
        df_new.to_excel(writer, index=False, sheet_name=new_sheet_name)

print(f'เพิ่มชีทใหม่ {num_sheets_to_add} ชีทเรียบร้อยแล้วในไฟล์ {file_name}')

