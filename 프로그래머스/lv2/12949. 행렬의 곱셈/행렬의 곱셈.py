def solution(arr1, arr2):
    mn=len(arr2[0])
    mx=len(arr1)
    answer = [[0]*(mn) for _ in range(mx)]
    for i in range(mx):
        for j in range(mn):
            for k in range(len(arr2)):
                answer[i][j]+=arr1[i][k]*arr2[k][j]
    return answer