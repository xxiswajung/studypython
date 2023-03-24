arr=list(map(str,input()))
stack=[]

for x in arr:
    if x.isdecimal():
        stack.append(int(x))
    elif x == '+':
        res = stack.pop(-2)+stack.pop()
        stack.append(res)
    elif x == '-':
        res = stack.pop(-2)-stack.pop()
        stack.append(res)
    elif x == '*':
        res = stack.pop(-2)*stack.pop()
        stack.append(res)
    elif x == '/':
        res = stack.pop(-2)/stack.pop()
        stack.append(res)
print(stack[0])
