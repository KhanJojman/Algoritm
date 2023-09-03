def canWin(n, m):
    if m % 2 == 0 and n % 2 == 0:
        return "Loose"
    elif m % 2 != 0 and n % 2 == 0:
        return "Win"
    else:
        return "Win"


n, m = map(int, input().split())
result = canWin(n, m)
print(result)