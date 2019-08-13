N = int(input())
d = [int(input()) for i in range(N)]

d.sort(reverse=True)
mochi = 101
kagami = 0

for i in d:
    if mochi > i:
        mochi = i
        kagami += 1

print(kagami)