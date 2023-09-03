import math

n, k = map(int, input().split())
result = math.factorial(n + k - 1) // (math.factorial(k) * math.factorial(n - 1))
print(result)