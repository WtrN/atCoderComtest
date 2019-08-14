n = int(input())
p = list(map(int, input().split()))
ans = 0

for i in range(1, n+1):
    if p[i-1] != i:
        ans += 1

if ans == 2 or ans == 0:
    print('YES')
else:
    print('NO')
