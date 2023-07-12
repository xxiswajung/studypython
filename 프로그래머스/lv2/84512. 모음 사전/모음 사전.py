#단어의 총 개수가 적어 전부 다 구해도 DFS보다 실행시간이 적음

from itertools import product #중복 순열

def solution(word):
    words=[]
    for i in range(1,6):
        for c in product(['A','E','I','O','U'], repeat=i):
            words.append(''.join(c))
    words.sort()
    return words.index(word)+1

##########################################
#처음엔 DFS로 풀려고 했으나, 실행시간이 더 길고 정답을 발견한 시점에서 바로 answer를 return 하지 못함

answer = 0
count = 0
arr = ['A','E','I','O','U']
def DFS(string, word):
    global count, answer
    
    if string==word:
        answer = count
        return
    if len(string)>5:
        return
    count+=1
    
    for i in arr:
        DFS(string+i, word)

def solution(word):
    DFS('',word)
    return answer
