arr=input()
stack=[]
sum=0

for i in range(len(arr)):
    if arr[i]=='(':
        stack.append(arr[i])
    else:
        stack.pop()
        if arr[i-1]=='(': #레이저 일 때
            sum+=len(stack)
        else: #막대가 끝났을 때
            sum+=1
print(sum)
