N = int(input())
S = list(input())
flg = False

if len(S) == 1:
    flg = False

elif len(S)%2 == 1:
    flg = False
else:
    num = len(S) // 2

    for i in range(num):
        if S[i] == S[i+num]:
            flg = True
        else:
            flg = False
            break

if flg == True:
    print("Yes")

else:
    print("No")