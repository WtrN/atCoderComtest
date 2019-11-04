N = int(input())

if N == 1:
    ans = 1.000000000
elif N%2 == 0:
    ans = 0.5
else:
    ans = (-(-N//2))/N

print(ans)