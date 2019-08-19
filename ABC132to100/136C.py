N = int(input())
H = list(map(int, input().split()))

for i in range(0, N-1):
    if H[N-1-i-1] - H[N-1-i] == 1:
        H[N-1-i-1] -= 1
    elif  H[N-1-i-1] - H[N-1-i] > 1:
        print('No')
        break
else:
    print('Yes')