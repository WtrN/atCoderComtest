N = int(input())
S = [list(input().split()) for i in range(N)]
mydict = dict(S)

check = sorted(mydict, key = lambda x:x[0])
result = [for i in range(1, N+1):i]

for i in range(N):
    