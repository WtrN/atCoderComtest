n, a, b = map(int, input().split())

train = n*a

if train > b:
    print(b)
else:
    print(train)