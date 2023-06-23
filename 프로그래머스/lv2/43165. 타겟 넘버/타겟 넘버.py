answer = 0
def DFS(v,numbers,target,sum):
    global answer
    # if sum>target:
    #     return
    if v==len(numbers):
        if sum==target:
            answer+=1
    else:
        DFS(v+1,numbers,target,sum+numbers[v])
        DFS(v+1,numbers,target,sum-numbers[v])
    
def solution(numbers, target):
    DFS(0,numbers,target,0)
    return answer