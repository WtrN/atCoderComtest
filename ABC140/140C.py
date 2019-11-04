N = int(input()) -1
B = list(map(int, input().split()))
ans = 0

if N == 1:
    ans = B[0]*2
else:
    ans += B[0] #min(B[0], B[1])

    num = 0
    for i in range(1, N-1):
        ans += min(B[i-1], B[i])
    else:
        ans += min(B[N-2], B[N-1])
        ans += B[N-1]

print(ans)
