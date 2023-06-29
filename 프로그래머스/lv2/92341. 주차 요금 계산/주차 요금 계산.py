import math

def get_fee(minutes,fees):
    return fees[1]+math.ceil(max(0,minutes-fees[0])/fees[2])*fees[3]

def solution(fees, records):
    parking={}
    stack={}
    
    for x in records:
        time, car, stat = x.split(' ')
        hour, minute = time.split(':')
        minutes = int(hour)*60+int(minute)
        
        if stat=='IN':
            parking[car]=minutes
        elif stat=='OUT':
            try:
                stack[car]+=minutes-parking[car]
            except:
                stack[car]=minutes-parking[car]
            del parking[car]
    for car, minute in parking.items():
        try:
            stack[car]+=23*60+59-minute
        except:
            stack[car]=23*60+59-minute
    return [get_fee(minutes, fees) for car, minutes in sorted(stack.items(), key=lambda x:x[0])]
            