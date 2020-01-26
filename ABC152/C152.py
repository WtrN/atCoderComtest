N = int(input())
P = list(map(int, input().split()))

num = P[0]
ans = 1

for i in range(1, N):
    if num > P[i]:
        num = P[i]
        ans += 1

print(ans)