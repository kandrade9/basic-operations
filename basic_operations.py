def basic_op(operator, value1, value2):
    if operator == "+":
        result = value1 + value2
        return result
    elif operator == "-":
        result = value2 - value1
        return result
    elif operator == "*":
        result = value1 * value2
        return result
    elif operator == "/":
        result = value1 / value2
        return result

user_op = input("Operator (+, -, *, /): ")
val1 = int(input("First value: "))
val2 = int(input("Second value: "))

print(basic_op(user_op, val1, val2))
