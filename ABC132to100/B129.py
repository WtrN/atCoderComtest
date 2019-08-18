N = int(input())
W = list(map(int, input().split()))
sum = 0
mini = 0

for i in W:
    sum += i

mini = sum
prefix_mini= 0

for i in W:
    prefix_mini += i
    mini = min(mini, abs(prefix_mini - (sum - prefix_mini)))

print(mini)