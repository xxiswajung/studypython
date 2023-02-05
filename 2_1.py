a,b = input().split()
count = 0

a = int(a)
b = int(b)

// this can be converted to 
// a,b = map(int,input().split())

for i in range(1,a):
    if a % i == 0:
        count += 1
        if count == b:
            print(i)

if count < b :
    print(-1)
    
// this can be converted to
// else :
//    print(-1)
