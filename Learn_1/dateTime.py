import datetime
time1 = [2023,1,1,0,0,1]
result = ''
def countdown(*args):
    day = [i for i in args]
    day1 = str(time1[0]-day[0])+'-'+str(day[1]-time1[1])+'-'+str(day[2]+time1[2])+' '+str(day[3]-time1[3])+':'+str(day[4]-time1[4])+':'+str(day[5])
    return day1

while True:
    y =datetime.datetime.now().year
    m =datetime.datetime.now().month
    d =datetime.datetime.now().day
    h =datetime.datetime.now().hour
    mi=datetime.datetime.now().minute
    s =datetime.datetime.now().second

    time2 = str(y)+'-'+str(m)+'-'+str(d)+' '+str(h)+':'+str(mi)+':'+str(s)
    if time2 != result:
        result = time2
        print(countdown(y,m,d,h,mi,s))
    if result == time1:
        break

