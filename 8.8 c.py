def calculate_expression(s):
    precedence = {
        "+": 1,
        "-": 1,
        "*": 2,
        "(": 3,
        ")": -1,
    }  # словарь для определения приоритета операций
    stack = []
    output = []

    for char in s:
        if char.isdigit():  # если текущий символ число, добавляем его в выходную строку
            output.append(char)

        elif char in ["+", "-", "*"]:  # если текущий символ операция
            while (
                stack and stack[-1] != "(" and precedence[char] <= precedence[stack[-1]]
            ):
                output.append(stack.pop())

            stack.append(char)

        elif (
            char == "("
        ):  # если текущий символ открывающая скобка, добавляем его в стек
            stack.append(char)

        elif char == ")":  # если текущий символ закрывающая скобка
            while stack and stack[-1] != "(":
                output.append(stack.pop())

            if stack and stack[-1] == "(":
                stack.pop()

    while stack:  # добавляем оставшиеся операции из стека в выходную строку
        output.append(stack.pop())

    # вычисляем значение выражения, используя стек
    for char in output:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == "+":
                result = operand1 + operand2
            elif char == "-":
                result = operand1 - operand2
            elif char == "*":
                result = operand1 * operand2

            stack.append(result)

    return stack.pop()  # возвращаем значение выражения


# Ввод данных
s = input()

# Вычисление и вывод результата
result = calculate_expression(s)
print(result)

# Не работает
