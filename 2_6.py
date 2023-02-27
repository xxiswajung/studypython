n=int(input())

def digit_sum(x):
    sum=0
    while x > 0:
        sum = sum + x%10
        x = x // 10
    return sum

maxlist=[]
arr=list(map(int,input().split()))

/* 내가 푼 방식 ->최대값을 뽑겠다고 불필요한 리스트를 또 생성할 필요는 없다 */

for x in arr :
    maxlist.append(digit_sum(x))

maxi=max(maxlist)

for index, res in enumerate(maxlist):
    if maxi == res :
        print(arr[index])
        break
        
/* 풀이 */

for x in arr:
    res = digit_sum(x)
    if max < res :
        max = res
        p = x
print(p)
