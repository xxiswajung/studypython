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

    
#More compact
# def check(a):
#     for i in range(9): #행과 열 체크
#         ch1=[0]*10
#         ch2=[0]*10
#         for j in range(9):
#             ch1[a[i][j]]=1
#             ch2[a[j][i]]=1
#         if sum(ch1)!=9 or sum(ch2)!=9:
#             return False
#     for i in range(3): #3x3 정사각형 체크
#         for j in range(3):
#             ch3=[0]*10
#             for k in range(3):
#                 for s in range(3):
#                     ch3[a[i*3+k][j*3+s]]=1
#             if sum(ch3)!=9:
#                 return False
#     return True

# a = [list(map(int,input().split())) for _ in range(9)]

# if check(a):
#     print("YES")
# else:
#     print("NO")
