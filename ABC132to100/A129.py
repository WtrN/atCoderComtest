p, q ,r = map(int, input().split())

r1 = p + q
r2 = q + r
r3 = p + r

print(min(r1, r2, r3))