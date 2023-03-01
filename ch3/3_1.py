n=int(input())

for i in range(n):
    a = input()
    a = a.lower()
    b = len(a)//2
    cnt = 0
    for j in range(b):
        if a[0+j]!=a[-1-j]:
            print('#'+str(i+1)+' NO',end='\n')
            cnt += 1
            break
    if cnt == 0:
        print('#'+str(i+1)+' YES',end='\n')
