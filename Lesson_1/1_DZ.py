"""1. Створіть дві змінні first=10, second=30. Виведіть на екран результат математичної взаємодії
      (+, -, *, / и тд.) для цих чисел."""
print ("------------------Home Task number 1 (Arithmetic operations)")
first_var = 10
second_var = 30
result = first_var + second_var
print(f'SUM : {first_var} + {second_var} =', result)
result = first_var - second_var
print(f'SUBTRACTION : {first_var} - {second_var} =', result)
result = first_var * second_var
print(f'MULTIPLICATION : {first_var} * {second_var} = ', result)
result = first_var ** second_var
print(f'EXPONENTIATION : {first_var} ** {second_var} = ', result)
result = first_var / second_var
print(f'DIVISION : {first_var} / {second_var} = ', result)
result = first_var // second_var
print(f'INTEGER DIVISION : {second_var} // {first_var} = ',  result)
result = first_var % second_var
print(f'REMAINDER OF DEVISION : {first_var} % {second_var} = ', result)

""" 2. Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 
      Виведіть на екран результат кожного порівняння."""
print ("------------------Home Task number 2 (Сomparison operations)")
first_var = 10
second_var = 30
result = first_var < second_var
print(f'{first_var} < {second_var} ?', result)
result = first_var > second_var
print(f'{first_var} > {second_var} ?', result)
result = first_var == second_var
print(f'{first_var} == {second_var} ?', result)
result = first_var != second_var
print(f'{first_var} != {second_var} ?', result)
result = first_var <= second_var
print(f'{first_var} <= {second_var} ?', result)
result = first_var >= second_var
print(f'{first_var} >= {second_var} ?', result)


""" З. Створіть змінну - резкльтат конкатенації строк "Hello " та "world!".  """
print ("------------------Home Task number 3 (Concatenation)")
word_1 = "Hello"
word_2 = "world!"
print(f'Type 1 : {word_1} {word_2}')
result_sentence = word_1 + " " + word_2
print("Type 2 :", result_sentence)
