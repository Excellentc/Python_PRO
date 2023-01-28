"""Сформуйте стрінг, в якому міститься інформація про певне слово. \
"Word [тут слово] has [тут довжина слова, отримайте з самого сдлва] letters",
наприклад "Word 'Python' has 6 letters".
Для отримання слова для аналізу скористайтеся константою або функцією input()."""

# word = input('Input you word, please: ')
# if word.isalpha() is False:
#     print('You entered an invalid value.\nTry again. Only letters, only 1 word.')
# else:
#     screen_input = 'Word \'{}\' has {} letters"'
#     result = screen_input.format(word.title(), len(word))
#     print(result)

"""Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік
  (можно використати константу або функцію input(), на екран має бути виведено лише одне повідомлення,
   також подумайте над варіантами, коли введені невірні дані).
        якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
        якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
        якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
        якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
        у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!" """

user_age = input('Input your age, only numbers please: ')
if not user_age.isdigit():
    print('You entered an invalid value. Try again. Input only numbers.')
else:
    user_age_int = int(user_age)                      # Cмена типа для переменной, для будущих арифметических сравнений
    if user_age.find('7') >= 0:                       # Проверка условия есть ли 7 рка в возрасте
        print(f'You are will be lucky today')
    elif 0 < user_age_int < 7:                        # Проверка условия 0 < x < 7
        print('Where are your parents?')
    elif 7 <= user_age_int < 16:                      # Проверка условия 7 =< x < 16
        print('This is an adult movie!')
    elif 16 <= user_age_int <= 65:                    # Проверка условия 16 <= x <= 65
        print('There are no more tickets!')
    elif 65 < user_age_int < 105:                     # Проверка условия   105 > x > 65
        print('Show your pension certificate!')
    elif user_age_int == 0 or user_age_int >= 105:    # Проверка граничных условий: если введен 0 или >= 105 лет
        print("Liar. People Don't live with this age")
