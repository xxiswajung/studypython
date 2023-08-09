def change(info):
    info = info.replace('C#','H')
    info = info.replace('D#','I')
    info = info.replace('F#','J')
    info = info.replace('G#','K')
    info = info.replace('A#','L')
    return info

def solution(m, musicinfos):
    answer = ''
    flag = 0 
    max_song = 0 
    m=change(m)
    for x in musicinfos:
        start, end, name, info = x.split(',')
        info = change(info)
        hour = int(end[:2]) - int(start[:2])
        minute = int(end[3:]) - int(start[3:])
        if minute < 0 :
            hour-=1
            minute += 60
        length = hour*60 + minute
        a = len(info)
        if a > length :
            info = info[:length]
        elif a < length :
            info = info*(length//a) + info[:length%a]
        
        if m in info and max_song<length:
            flag = 1
            max_song=length
            answer=name
    if flag == 1:
        return answer
    else :
        return "(None)"