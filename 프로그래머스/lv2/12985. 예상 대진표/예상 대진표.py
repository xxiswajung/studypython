def solution(n,a,b):
    answer = 1
    rnd = 0
    while n!=1:
        n=n//2
        rnd+=1
    for _ in range(rnd):
        if min(a,b)%2==1 and max(a,b)-min(a,b)==1:
            return answer
        else:
            if a%2==1:
                a=(a+1)//2
                if b%2==1:
                    b=(b+1)//2
                    answer+=1
                else:
                    b=b//2
                    answer+=1
            else:
                a=a//2
                if b%2==1:
                    b=(b+1)//2
                    answer+=1
                else:
                    b=b//2
                    answer+=1
            