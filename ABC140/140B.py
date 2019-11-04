N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
be = 22
cu = 0

for i in range(N):
    cu = A[i] -1
    ans += B[cu]
    if cu == be+1:
        ans += C[be]
    
    be = cu
print(ans)