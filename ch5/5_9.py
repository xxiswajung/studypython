p=dict()

a=input()
for x in a:
    if x in p:
        p[x]+=1
    else:
        p[x]=1
b=input()
for x in b:
    p[x]-=1

if all(value == 0 for value in p.values()):
    print("YES")
else:
    print("NO")
    
#딕셔너리의 내장함수 get 이용하기
#초기의 value값은 초기화 되어있지 않아 누적이 안되기 때문

a=input()
b=input()
str1=dict()
for x in a:
    str1[x]=str1.get(x,0)+1
for x in b:
    str1[x]=str1.get(x,0)-1

for x in a:
    if str1.get(x)>0:
        print("NO")
        break
else:
    print("YES")
