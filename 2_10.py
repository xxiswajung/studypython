n = int(input())
arr = list(map(int,input().split()))
cnt = [0]*n

if arr[0] == 1 :
    cnt[0] == 1
for i in range(n):
    if arr[i] == 0 :
        continue
    else:
        if arr[i]==1 and arr[i-1]==1:
            cnt[i] = cnt[i-1]+1
        else:
            cnt[i] = 1
print(sum(cnt))
