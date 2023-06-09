def solution(k, tangerine):
    answer = 0 
    nn={} #use dictionary rather than tuple
    for i in tangerine: #initialize the dictionary
        nn[i]=0
    for i in tangerine: #count the number of each tangerine 
        nn[i]+=1
    nn=sorted(nn.items(),key=lambda x:x[1],reverse=True)
    
    cnt=0
    for i in nn:
        k-=i[1]
        answer+=1
        if k<=0:
            return answer