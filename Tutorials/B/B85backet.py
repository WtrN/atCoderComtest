N = int(input())
d = [int(input()) for i in range(N)]

num = [0]*110
res = 0

for i in d:
    num[i] += 1

for i in range(110):
    if num[i] > 0:
        res+=1
print(res)