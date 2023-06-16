def solution(clothes):
    answer = 1
    dict={}
    for i in clothes:
        dict[i[1]]=0
    for i in clothes:
        dict[i[1]]+=1
    for x in dict:
        answer*=(dict[x]+1)
    return answer-1
