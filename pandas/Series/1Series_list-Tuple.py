import pandas as pd
data_ls = [10,20,30,'phol1',True]
data_lp = [30,20,10,'phol2',False]
ps = pd.Series(data_ls)
ps1 = pd.Series(data_lp)
print(ps)
idx = [50,20,30,5,6]
ps = pd.Series(data_ls,index=idx) #อินเดก และจำนวนข้อมูลต้องเท่ากัน
print(ps)