def calculate_expression(s):
    stack = []
    i = 0

    while i < len(s):
        if s[i].isdigit():  # если текущий символ число
            num = 0

            while i < len(s) and s[i].isdigit():  # считываем все цифры числа
                num = num * 10 + int(s[i])
                i += 1

            stack.append(num)  # добавляем число в стек

        elif s[i] in ["+", "-", "*"]:  # если текущий символ операция
            op = s[i]

            if op == "+":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 + operand2

            elif op == "-":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 - operand2

            elif op == "*":
                operand2 = stack.pop()
                operand1 = stack.pop()
                result = operand1 * operand2

            stack.append(result)  # добавляем результат операции в стек

            i += 1

        else:
            i += 1

    return stack.pop()  # возвращаем значение выражения


# Ввод данных
s = input()

# Вычисление и вывод результата
result = calculate_expression(s)
print(result)

# Не работает
