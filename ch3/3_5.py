n, m=map(int, input().split())
a=list(map(int, input().split()))
lt=0
rt=1
tot=a[0] #부분배열의 합을 첫번째 원소로 초기화, 이때 구간은 lt ~ (rt-1) 구간
cnt=0
while True:
    if tot<m: #부분배열의 합이 아직 작을때
        if rt<n: #오른쪽 구간이 배열의 길이 안에 속할 때
            tot+=a[rt]
            rt+=1
        else: #오른쪽 구간이 배열의 길이를 벗어날때
            break #반복문 종료
    elif tot==m: #부분배열의 합이 같을때
        cnt+=1
        tot-=a[lt] #왼쪽 구간의 원소를 부분배열의 합에서 삭제하고
        lt+=1 #왼쪽구간 한칸 앞으로
    else: #부분배열의 합이 너무 클때
        tot-=a[lt] #왼쪽 구간의 원소를 부분배열의 합에서 삭제하고
        lt+=1 #왼쪽구간 한칸 앞으로 (왜냐하면 이제 그쪽은 볼 필요 없기 때문)
print(cnt)
