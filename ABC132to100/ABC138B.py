N = int(input())
a = list(map(float, input().split()))
result = 0.

for i in a:
    result += 1./i

print(1/result)