def solution(sequence, k):
    answer = []
    n = len(sequence)
    j = 0
    s = 0
    for i in range(n):
        while s < k and j < n:
            s+=sequence[j]
            j+=1
        if s == k :
            answer.append([i,j-1])
        s-=sequence[i]
    return sorted(answer,key=lambda x:x[1]-x[0])[0]