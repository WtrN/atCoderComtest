N, X = map(int, input().split())
L = list(map(int, input().split()))

dis = 0
count = 1

for i in range(1, N+1):
    dis = dis + L[i-1]
    if dis <= X:
        count += 1

print(count)