def binary(t):
    ans=''
    if t==0:
        return True
    elif t==1:
        return '1'+ans
    else:
        while t>0:
            ans=str(t//2)+ans
            t=t%2

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