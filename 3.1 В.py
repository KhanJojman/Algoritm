from math import comb

n, k = map(int, input().split())
result = comb(n, k)
print(result)