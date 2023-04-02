#재귀를 이용한 깊이우선탐색

def DFS_1(v): #전위순회
    if v>7:
        return
    else:
        print(v,end=' ') #부모, 자기자신
        DFS_1(v*2) #왼쪽자식
        DFS_1(v*2+1) #오른쪽 자식

def DFS_2(v): #중위순회
    if v>7:
        return
    else:
        DFS_2(v*2) #왼쪽자식
        print(v,end=' ') #부모, 자기자신
        DFS_2(v*2+1) #오른쪽 자식

def DFS_3(v): #후위순회
    if v>7:
        return
    else:
        DFS_2(v*2) #왼쪽자식
        DFS_2(v*2+1) #오른쪽 자식
        print(v,end=' ') #부모, 자기자신


if __name__=="__main__":
    print("전위순회 : 부모 -> 왼쪽자식 -> 오른쪽자식")    
    DFS_1(1)
    print()
    print("중위순회 : 왼쪽자식 -> 부모 -> 오른쪽자식")
    DFS_2(1)
    print()
    print("후위순회 : 왼쪽자식 -> 오른쪽자식 -> 부모")
    DFS_3(1)
