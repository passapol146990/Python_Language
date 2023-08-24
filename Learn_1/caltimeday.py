secund = int(input('input secund time :'))
def secund_time(secund):
    d,h,m,s = 0,0,0,0
    if(secund >= 86400):
        d = secund//86400
        secund = secund%86400 
    if(secund >= 3600 ):
        h = secund//3600 
        secund = secund%3600
    if(secund >= 60):
        m = secund//60
        secund = secund%60
    if(secund >= 1):
        s = secund//1
    print('day = ',d,'hour = ',h,'minute = ',m,'second = ',s)

secund_time(secund)    



"""
1 secund = 1
1 minute = 60
1 hour = 3600
1 day = 86400
"""

