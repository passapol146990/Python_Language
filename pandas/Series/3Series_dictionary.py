import pandas as pd
datad = {1:'phol1', 2:'phol2', 3:'phol3'}
idx = [3,2,1]
pdi = pd.Series(datad,index=idx)
print(pdi)