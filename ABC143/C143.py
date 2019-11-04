N = int(input())
S = list(input())
sum = 1

for i in range(1, N):
    if S[i-1] != S[i]:
        sum += 1

print(sum)