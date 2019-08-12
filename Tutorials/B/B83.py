n, a, b = map(int, input().split())
count = 0
sum = 0

for i in range(1, n+1):
    sum=0
    while i > 0:
        sum += i%10
        i = i//10
    print(sum)
    if sum >=a and sum <=b:
        count += i

print(count)