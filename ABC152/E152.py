import math
def if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split())
    print(lcm(a))


def lcm(a):
    from fractions import gcd
    x = a[0]
    for i in range(1, len(a)):
        x = (x * a[i]) // gcd(x, a[i])
    return x

