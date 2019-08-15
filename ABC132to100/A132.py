s1, s2, s3, s4 = input()
s = [s1, s2, s3, s4]

s.sort()

if s[0] == s[1] and s[1] != s[2] and s[2] == s[3]:
    print('Yes')
else:
    print('No')