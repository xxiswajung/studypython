n=int(input())

def digit_sum(x):
    # length=len(x)
    sum=0
    while x > 0:
        sum = sum + x%10
        x = x // 10
    return sum

maxlist=[]
arr=list(map(int,input().split()))


for x in arr :
    maxlist.append(digit_sum(x))
# maxlist.append(digit_sum(arr[i]))

maxi=max(maxlist)

for index, res in enumerate(maxlist):
    if maxi == res :
        print(arr[index])
        break
