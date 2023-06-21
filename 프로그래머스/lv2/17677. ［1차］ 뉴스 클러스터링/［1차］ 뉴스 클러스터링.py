def solution(str1, str2):
    s1=[]
    s2=[]
    for i in range(len(str1)-1):
        res=str1[i:i+2]
        if res.isalpha():
            s1.append(res.lower())
    for i in range(len(str2)-1):
        res=str2[i:i+2]
        if res.isalpha():
            s2.append(res.lower())
    
    m1=set(s1)&set(s2)
    m2=set(s1)|set(s2)
    
    m11=sum([min(s1.count(word),s2.count(word)) for word in m1])
    m22=sum([max(s1.count(word),s2.count(word)) for word in m2])
    
    if m22==0:
        return 65536
    else:
        return int(m11/m22*65536)