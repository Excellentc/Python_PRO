"""Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік
  (можно використати константу або функцію input(), на екран має бути виведено лише одне повідомлення,
   також подумайте над варіантами, коли введені невірні дані).
        якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
        якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
        якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
        якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
        у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!" """

user_age = input('Input your age, only numbers please: ')
user_age_int = int(user_age)                                # смена типа для переменной, для будущих сравнений
lucky_guy_msg = ''
if user_age.find('7') >= 0:
    lucky_guy_msg = 'You are will be lucky today!'          # присвоение переменной для счастливчика
if not user_age.isdigit():
    print('You entered an invalid value. Try again. Input only one numbers .')
else:
    if 0 < user_age_int < 7:                            # Проверка условия 0 < x < 7
        print('Where are your parents?')
    elif 7 <= user_age_int < 16:                        # Проверка условия 7 =< x < 16
        print(f'This is an adult movie! {lucky_guy_msg}')
    elif 16 <= user_age_int <= 65:                      # Проверка условия 16 <= x <= 65
        print(f'There are no more tickets! {lucky_guy_msg}')
    elif 65 < user_age_int < 105:                       # Проверка условия 65 < x < 105
        print(f'{lucky_guy_msg} Show your pension certificate! ')
    elif user_age_int == 0 or user_age_int >= 105:      # Проверка граничных условий: если введен 0 или >= 105 лет
        print("Liar. People Don't live with this age")
