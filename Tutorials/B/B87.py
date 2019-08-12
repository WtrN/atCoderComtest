a = int(input())
b = int(input())
c = int(input())
x = int(input())
count = 0

for ia in range(a+1):
    for ib in range(b+1):
        for ic in range(c+1):
            if x == (500*ia + 100*ib + 50*ic):
                count+=1

print(count)