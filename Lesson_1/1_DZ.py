"""1. Створіть дві змінні first=10, second=30. Виведіть на екран результат математичної взаємодії
      (+, -, *, / и тд.) для цих чисел."""
print ("------------------Home Task number 1 (Arithmetic operations)")
first = 10
second = 30
print(f'SUM : {first} + {second} =', first + second)
print(f'SUBTRACTION : {first} - {second} =', first - second)
print(f'MULTIPLICATION : {first} * {second} = ', first * second)
print(f'EXPONENTIATION : {first} ** {second} = ', first ** second)
print(f'DIVISION : {first} / {second} = ', first / second)
print(f'INTEGER DIVISION : {second} // {first} = ',  second // first)
print(f'REMAINDER OF DEVISION : {first} % {second} = ', first % second)

""" 2. Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 
      Виведіть на екран результат кожного порівняння."""
print ("------------------Home Task number 2 (Сomparison operations)")
c = first < second
print(f'{first} < {second} ?', c)
c = first > second
print(f'{first} > {second} ?', c)
c = first == second
print(f'{first} == {second} ?', c)
c = first != second
print(f'{first} != {second} ?', c)
c = first <= second
print(f'{first} <= {second} ?', c)
c = first >= second
print(f'{first} >= {second} ?', c)


""" З. Створіть змінну - резкльтат конкатенації строк "Hello " та "world!".  """
print ("------------------Home Task number 3 (Concatenation)")
a = "Hello"
b = "world!"
print(f'Type 1 : {a} {b}')
c = a + " " + b
print("Type 3 :", c)