n=input()
arr = []
for i in range(len(n)):
    if ord(n[i]) < 65 or ord(n[i])> 122 :
        arr.append(n[i])

arr = ''.join(arr)
arr = int(arr)
cnt = 0

for j in range(1,arr+1):
    if arr % j == 0:
        cnt += 1
print(arr)
print(cnt)
