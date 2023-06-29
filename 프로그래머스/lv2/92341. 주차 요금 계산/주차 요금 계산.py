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

########################
#split을 좀 더 잘 활용해보자

import math

def get_fee(minutes, fees):
    return fees[1] + math.ceil(max(0, (minutes - fees[0])) / fees[2]) * fees[3]

def solution(fees, records):
    parking = dict()
    stack = dict()
    
    for record in records:
        time, car, cmd = record.split()
        hour, minute = time.split(":")
        minutes = int(hour) * 60 + int(minute) # 시간 -> 분 환산

        if cmd == 'IN':
            parking[car] = minutes
        elif cmd == 'OUT':
            try:
                stack[car] += minutes - parking[car]
            except:
                stack[car] = minutes - parking[car]
            del parking[car] # 출차 차량 삭제
    
    # 출차 기록 없는 차 23:59 출차 처리
    for car, minute in parking.items():
        try:
            stack[car] += 23*60+59 - minute
        except:
            stack[car] = 23*60+59 - minute
        
    return [get_fee(time, fees) for car, time in sorted(list(stack.items()), key=lambda x: x[0])]
