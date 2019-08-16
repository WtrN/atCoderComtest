n, l = map(int, input().split())
L = l
R = n+l-1
eat = 0

if L >= 0 : eat = L
elif R <= 0 : eat = R
else : eat = 0

sum = (R+L)*(R-L+1)/2 -eat
print(int(sum))

