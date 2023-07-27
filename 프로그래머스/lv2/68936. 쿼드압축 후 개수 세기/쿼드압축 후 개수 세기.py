def solution(arr):
    answer=[0,0]
    n = len(arr)
    
    def quadtree(x,y,n):
        start=arr[x][y]
        
        for i in range(x,x+n):
            for j in range(y,y+n):
                if arr[i][j]!=start:
                    n=n//2
                    quadtree(x,y,n)
                    quadtree(x,y+n,n)
                    quadtree(x+n,y,n)
                    quadtree(x+n,y+n,n)
                    return
                    
        answer[start]+=1
    
    quadtree(0,0,n)
    return answer