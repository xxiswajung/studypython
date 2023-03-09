s = [list(map(int,input().split())) for _ in range(9)]

arr=[1,2,3,4,5,6,7,8,9]
chk=[0]*9
flag = 0

for i in range(9):
    for j in arr:
        if j in s[i] :
            chk[j-1]+=1
        if chk[j-1]>=2:
            flag=1
    chk=[0]*9

for i in range(9):
    for k in range(9):
        for j in arr:
            if j == s[i][k]:
                chk[j-1]+=1
            if chk[j-1]>=2:
                flag=1
    chk=[0]*9

for k in [0,3,6]:
    for i in range(0,3):
        for t in range(0,3):
            for j in arr:
                if j == s[i+k][t+k] :
                    chk[j-1]+=1
                if chk[j-1]>=2:
                    flag=1
    chk=[0]*9

if flag == 0:
    print("YES")
else :
    print("NO")
