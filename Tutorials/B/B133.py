import numpy as np
import math
n, d = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]

narr = np.array(x)
ans = 0

for i in range(n):
    for j in range(i+1, n):
        dis = np.linalg.norm(narr[j] - narr[i])
        if math.ceil(dis) == math.floor(dis):
            ans += 1

print(ans)