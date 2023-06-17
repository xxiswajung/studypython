def solution(s):
    answer=[]
    s=sorted(s[2:-2].split('},{'), key=len)
    
    for i in s:
        j=i.split(',')
        for k in j:
            if int(k) not in answer:
                answer.append(int(k))
    return answer