res=''
def bin(n):
    global res
    if n==1:
        return '1'+res
    else:
        res=str(n%2)+res
        return bin(n//2)
    
n=int(input())
print(bin(n))
