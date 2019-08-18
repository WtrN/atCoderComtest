from collections import deque

N = int(input())
v = list(map(int, input().split()))
v.sort()
V = deque(v)
sum = 0
while True:
    sum = (V.popleft() + V.popleft())/2
    V.appendleft(sum)
    if len(V) == 1:
        break

print(V[0])
