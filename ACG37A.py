#ABCのCに相当する問題
S = input()
s = list(S)
num = 1
first = ''
List = []

for i in range(1, len(s)):
    print(s[i])
    if s[i-1] != s[i]:
        num += 1
        
    else:
        s[i+1] = s[i]+s[i+1]
        # print(s[i+1])
        # i+=1

print(num)