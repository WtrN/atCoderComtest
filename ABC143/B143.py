N = int(input())
d = list(map(int, input().split()))

sum = 0

for i in range(N):
    for j in range(N):
        if i != j and i < j:
            sum += d[i] * d[j]

print(sum)