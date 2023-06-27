def solution(n, t, m, p):
    answer = ''
    arr=[0]
    for i in range(1,t*m):
        res=''
        while i>0:
            i, j = divmod(i,n)
            if j==10:
                res+='A'
            elif j==11:
                res+='B'
            elif j==12:
                res+='C'
            elif j==13:
                res+='D'
            elif j==14:
                res+='E'
            elif j==15:
                res+='F'
            else:
                res+=str(j)
        res=res[::-1]
        for k in range(len(res)):
            arr.append(res[k])
    for i in range(t*m):
        if i%m==(p-1):
            answer+=str(arr[i])
    return answer