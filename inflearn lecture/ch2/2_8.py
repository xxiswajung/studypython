def reverse(x):
    res = 0
    while x > 0 : 
        res = res + (x % 10) * (10 ** (len(str(x))-1))
        # or 
        # t=x%10
        # res=res*10+t
        # 뒤에 있는 걸 누적으로 10 곱하는 방식 
        x = x // 10
    return res

def isPrime(x):
    cnt = 0
    for i in range(1,x+1):
        if x % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    # if x==1:
    #     return False
    # for i in range(2, x):
    #     if x%i==0:
    #         return False
    # return True

n = int(input())
arr = list(map(int,input().split()))

for x in arr :
    a = reverse(x)
    if isPrime(a):
        print(a, end=' ')
