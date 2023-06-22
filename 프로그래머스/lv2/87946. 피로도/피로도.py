answer = 0
res = 0
v = 0
ch = [0]*8

def solution(k,dungeons):
    global v, res, ch, answer
    for i in range(len(dungeons)):
        v+=1
        if ch[i]==0 and dungeons[i][0]<=k:
            ch[i]=1
            k-=dungeons[i][1]
            res+=1
            solution(k,dungeons)
            ch[i]=0
            k+=dungeons[i][1]
            res-=1      
            v-=1
        answer=max(res,answer)
    return answer


