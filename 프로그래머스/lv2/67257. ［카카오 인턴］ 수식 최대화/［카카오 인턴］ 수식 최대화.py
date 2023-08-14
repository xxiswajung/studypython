from itertools import permutations

def op(num1,num2,sym):
    if sym=='+':
        return str(int(num1)+int(num2))
    elif sym=='-':
        return str(int(num1)-int(num2))
    else:
        return str(int(num1)*int(num2))
    
def cal(exp,sym): # 매개변수 : expression 과 연산자 우선순위
    # 1. expression 안에 있는 숫자와 연산자를 차례대로 arr에 저장
    # ex) ['100','-','200','*','300','-','500','+','20']
    arr=[]
    tmp=''
    
    for i in exp:
        if i.isdigit():
            tmp+=i
        else:
            arr.append(tmp)
            arr.append(i)
            tmp=''
    arr.append(tmp)  
    
    #2. 우선순위가 높은 연산자 순 대로 expression 전체(=arr)를 탐색 해 그 연산자만 계산하고
    #모든 expression을 전부 봤으면, 다시 처음으로 돌아가 다음 우선순위 연산자에 해당하는 것만 계산한다. 
    for x in sym:
        stack=[]
        while arr:
            tmp=arr.pop(0)
            if tmp==x:
                stack.append(op(stack.pop(),arr.pop(0),x))
            else:
                stack.append(tmp)
        arr=stack #다음 우선순위의 연산자를 계산하기 위해 지금까지 계산된 expression이 담긴 stack을 arr로 옮겨준다. 
    
    return abs(int(arr[0]))

def solution(expression):
    symbol = ['-','+','*']
    symbol_arr=permutations(symbol,3)
    answer=0
    for i in symbol_arr:
        answer=max(answer,cal(expression,i))
    return answer