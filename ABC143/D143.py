N = int(input())
L = list(map(int, input().split()))

L.sort(reverse=True)
# print(L)
num = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(i+j+1,N):
            print(L[k])
            if L[i] < L[j] + L[k]:
                num += 1

print(num)