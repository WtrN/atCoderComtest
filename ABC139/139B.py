a,b = map(int, input().split())
ans = 0
flag = True

if b == 1:
    ans = 0
elif a >= b:
    ans = 1
else:
    ans += 1
    while(True):
        b = b - a
        if b <= 0:
            break
        else:
            ans += 1
            b += 1

print(ans)

# elif a == b or a >= b:
#     ans = 1
# else:
#     ans = -(-b//(a-1))