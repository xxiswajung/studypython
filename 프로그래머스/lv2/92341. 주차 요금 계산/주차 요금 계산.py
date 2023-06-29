import datetime, math

def solution(fees, records):
    answer = []
    car = []
    time = []
    dic = {}
    for x in records:
        xx=x.split(' ')
        if xx[2]=='IN':
            car.append(xx[1])
            time.append(xx[0])
        if xx[2]=='OUT':
            time1=datetime.datetime.strptime(xx[0],"%H:%M")
            time2=datetime.datetime.strptime(time[car.index(xx[1])],"%H:%M")
            ttime=time1-time2
            time.pop(car.index(xx[1]))
            car.pop(car.index(xx[1]))
            if xx[1] in dic:
                dic[xx[1]] += ttime.seconds//60
            else:
                dic[xx[1]] = ttime.seconds//60
    while car:
        time1='23:59'
        time1=datetime.datetime.strptime(time1,"%H:%M")
        time2=datetime.datetime.strptime(time[0],"%H:%M")
        ttime=time1-time2
        if car[0] in dic:
            dic[car[0]] += ttime.seconds//60
        else:
            dic[car[0]] = ttime.seconds//60 
        time.pop(0)
        car.pop(0)
    for car, tt in dic.items():
        if tt <= fees[0]:
            dic[car] = fees[1]
        else:
            dic[car] = fees[1]+math.ceil((tt-fees[0])/fees[2])*fees[3]
    dicc = dict(sorted(dic.items()))
    for car, tt in dicc.items():
         answer.append(tt)
    return answer