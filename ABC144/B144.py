N = int(input())
ans = 0

for i in range(1,10):
    for j in range(1, 10):
        if N == i*j:
            ans = 1

if ans == 1:
    print("Yes")
else:
    print("No")