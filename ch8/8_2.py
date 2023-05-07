def NOde(a):
    if dy[a]>0:
        return dy[a] #cut edge
    if a==1 or a==2:
        return a
    else:
        dy[a]=NOde(a-1)+NOde(a-2)
        return dy[a]

n=int(input())
dy=[0]*(n+1) #memoization 
print(NOde(n))
