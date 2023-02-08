#temporary add code

n = int(input())
arr = list(map(int,input().split()))

avg = round(sum(arr) / n)
arr2 = list()

for i in arr:
    arr2.append(abs(i-avg))
min_2 = min(arr2)

print(arr2)
