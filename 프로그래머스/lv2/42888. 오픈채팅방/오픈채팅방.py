def solution(record):
    answer = []
    dd = {}
    for x in record:
        if x[0]=="E" or x[0]=="C":
            status, uid, name = x.split(' ')
            dd[uid]=name
    for x in record:
        if x[0]=="E":
            status, uid, name = x.split(' ')
            answer.append(dd[uid]+"님이 들어왔습니다.")
        elif x[0]=="L":
            status, uid= x.split(' ')
            answer.append(dd[uid]+"님이 나갔습니다.")
    return answer