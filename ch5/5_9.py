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
