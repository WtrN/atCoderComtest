N = int(input())
card = list(map(int, input().split()))

Alice = 0
Bob = 0

card.sort(reverse =True)

j = 0
for i in card:
    if j % 2 == 0:
        Alice += i
    else:
        Bob += i
    j +=1

print(Alice-Bob)