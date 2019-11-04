A, B = map(int, input().split())
B = B*2

if B > A:
    print(0)
else:
    print(A-B)