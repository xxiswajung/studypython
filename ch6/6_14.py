import sys
sys.stdin=open("input.txt","r")

n,m=map(int,input().split())
ch=[[0]*n for i in range(n)]
#ch=[[0]*n]*n 은 얕은 복사(단순 복사)를 하기 때문에 바라보는 객체가 동일. 따라서 하나가 바뀌면 전부 바뀌므로 사용 X
for i in range(m):
    a,b,c=map(int,input().split())
    ch[a-1][b-1]=c

for x in ch:
    for j in x:
        print(j,end=' ')
    print()
