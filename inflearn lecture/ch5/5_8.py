n=int(input())
a=[]
b=[]
for i in range(n):
    a.append(input())
for i in range(n-1):
    b.append(input())

for i in range(n-1):
    if b[i] in a:
        c=a.index(b[i])
        a.pop(c)

print(a[0])

##########################
#using dictionary#

n=int(input())
a=dict()

for i in range(n):
    word=input()
    a[word]=1
for i in range(n-1):
    word=input()
    a[word]=0

for key, val in a.items():
    if val==1:
        print(key)
        break
