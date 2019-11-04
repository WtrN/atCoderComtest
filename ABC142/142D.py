A, B = map(int, input().split())
ans = 1

for k in range(2,B+1):
    
    if pow(2, k-1, k) == 1:
        if A%k == 0 and B%k == 0:
            ans += 1
print(ans)




# num = list()
# num.append(1)
# ans = 1

# for i in range(2, A):
#     if A%i == 0 and B%i == 0:
#         for j in num:
#             if i % j == 0 and j!=1:
#                 break
#         else:
#             num.append(i)
#             ans += 1
# print(ans)