N = int(input())
H = list(map(int, input().split()))
num = 0
ans = 0


for j in range(1, N):
    if H[j-1] >= H[j]:
        num +=1
        # print(num)
    else:
        if num > ans:
            ans = num
        num = 0
else:
    if num > ans:
        ans = num



print(ans)