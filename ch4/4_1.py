n,m=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
print(arr.index(m)+1)

#정석 pseudo code를 문제에 맞게 수정하면

# n, m=map(int, input().split())
# a=list(map(int, input().split()))
# a.sort()
# lt=0
# rt=n-1
# while lt<=rt:
#     mid=(lt+rt)//2
#     if a[mid]==m:
#         print(mid+1)
#         break
#     elif a[mid]>m:
#         rt=mid-1
#     else:
#         lt=mid+1
