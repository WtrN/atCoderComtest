N = int(input())
s = [input() for i in range(N)]
ans ={}
num = 0

for i in range(N):
    s[i] = ''.join(sorted(s[i]))
    if s[i] in ans.keys():
        ans[s[i]] += 1
        num += ans[s[i]]
    else:
        ans[s[i]] = 0

print(num)