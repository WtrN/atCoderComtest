N, Y = map(int, input().split())

res10k = -1
res5k = -1
res1k = -1

for i in range(N+1):
    for j in range(N+1-i):
        k = N - i - j
        if Y == i*10000 + j*5000 + k*1000:
            res10k = i
            res5k = j
            res1k = k

print(res10k, res5k, res1k)