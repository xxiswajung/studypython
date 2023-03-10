arr = [list(map(int,input().split())) for _ in range(7)]
cnt = 0
lt=0
rt=4

for i in range(7):
    for j in range(3):
        if arr[i][lt+j]==arr[i][rt+j] and arr[i][lt+j+1]==arr[i][rt+j-1]:
            cnt+=1
        if arr[lt+j][i]==arr[rt+j][i] and arr[lt+j+1][i]==arr[rt+j-1][i]:
            cnt+=1

print(cnt)

#list 반대로 = arr[::-1]
