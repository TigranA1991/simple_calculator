first_operand = int(input('Enter first number: '))
math_operation = input('Enter mathematical operation: ')
second_operand = int(input('Enter second operand: '))
result = 0

if math_operation == '+':
    result = first_operand + second_operand
elif math_operation == '-':
    result = first_operand - second_operand
elif math_operation == '*':
    result = first_operand * second_operand
elif math_operation == '/':
    result = first_operand / second_operand

print(f'Result: {result}')