def gcd(a, b):
    # Вычисляем наибольший общий делитель с помощью алгоритма Евклида
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Вычисляем наименьшее общее кратное с помощью формулы НОК(a, b) = |a * b| / НОД(a, b)
    return abs(a * b) // gcd(a, b)

# Считываем значения из ввода
a, b = map(int, input().split())

# Вычисляем наименьшее общее кратное чисел a и b
result = lcm(a, b)

# Выводим результат
print(result)