import numpy as np

N, K, Q = map(int, input().split())
A = [int(input()) for i in range(N)]

point = np.array([K] * N)

for i in range(Q):
    point -= 1