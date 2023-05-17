n,k=map(int,input().split())
queue=[]

for i in range(1,n+1):
    queue.append(i)

while queue:
    for _ in range(k-1):
        cur=queue.pop(0)
        queue.append(cur)
    queue.pop(0)
    if len(queue)==1:
        print(queue[0])
        queue.pop()
