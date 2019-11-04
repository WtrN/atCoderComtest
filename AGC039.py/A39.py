S = list(input())
K = int(input())
ans = 0
i= 1

if len(S) == 1:
    ans = -(-K//2)
else:
    while i < len(S):
        if S[i-1] == S[i]:
            ans += 1
            i += 1
        i+=1
    ans *= K
    if len(S) != 1:
        if S[0] == S[len(S)-1] and S[len(S)-2] != S[len(S)-1]: ans += K -1
    if len(S) > 2:
        if S[0] == S[len(S)-1] and S[len(S)-3] == S[len(S)-2] == S[len(S)-1]: ans += K -1
        # elif S[0] == S[len(S)-1] and S[len(S)-2] == S[len(S)-1] and S[len(S)-2] == S[len(S)-3]: 



print(ans)