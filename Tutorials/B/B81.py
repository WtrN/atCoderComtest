N = int(input())
A = list(map(int, input().split()))
num = 0
flag = False
while True:
    for a in A:
        if a%2==1:
            flag = True
    
    if flag == True:
        break

    for i in range(len(A)):
        A[i] /= 2
    num+=1

print(num)