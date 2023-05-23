def solution(s):
    zero=0
    cnt=0
    answer = []
    while s!='1':
        zero=zero+s.count('0')
        s=s.replace('0','')
        s=format(len(s),'b')
        cnt+=1
    answer.append(cnt)
    answer.append(zero)
    return answer
