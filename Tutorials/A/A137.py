a, b = map(int, input().split())

sum = a+b
sub = a-b
mul = a*b
list = [sum, sub, mul]

print(max(list))