def solution(clothes):
    answer = 1
    res = 0
    dict={}
    for i in clothes:
        dict[i[1]]=0
    for i in clothes:
        dict[i[1]]+=1
    for x in dict:
        answer*=(dict[x]+1)
        res+=dict[x]
    if len(dict)==1:
        return res
    else:
        return answer-1