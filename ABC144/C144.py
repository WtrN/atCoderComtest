N = int(input())
ans = N -1
n = N//2
# print(n)

for i in range(1, n):
    print(i)
    n = N//i
    if N % i == 0:
        ans = min(ans, i+N//i-2)
        # print(ans)

print(ans)