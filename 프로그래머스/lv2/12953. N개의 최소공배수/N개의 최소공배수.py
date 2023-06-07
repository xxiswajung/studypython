def solution(arr):
    a=max(arr)
    b=1
    for x in arr:
        b*=x
    for i in range(a,b+1):
        if all(i % num == 0 for num in arr) is True:
                return i