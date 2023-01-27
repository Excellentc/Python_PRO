"""Сформуйте стрінг, в якому міститься інформація про певне слово. \
"Word [тут слово] has [тут довжина слова, отримайте з самого сдлва] letters",
наприклад "Word 'Python' has 6 letters".
Для отримання слова для аналізу скористайтеся константою або функцією input()."""

word = input('Input you word, please: ')
if word.isalpha() is False:
    print('You entered an invalid value.\nTry again. Only letters, only 1 word.')
else:
    screen_input = 'Word \'{}\' has {} letters"'
    result = screen_input.format(word.title(), len(word))
    print(result)

"""Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік
  (можно використати константу або функцію input(), на екран має бути виведено лише одне повідомлення,
   також подумайте над варіантами, коли введені невірні дані).
        якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
        якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
        якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
        якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
        у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!" """

user_age = input('Input your age , please: ')
if user_age.isdigit() is False:
    print('You entered an invalid value.\nTry again. Input only numbers .')
else:
    if user_age.find('7') >= 0:
        print('You are lucky today!')
    user_age1 = int(user_age)
    if 0 < user_age1 < 7:
        print('Where are your parents?')
    elif 7 <= user_age1 < 16:
        print('This is an adult movie!')
    elif user_age1 > 65:
        print('Show your pension certificate!')
    elif 16 <= user_age1 <= 65:
        print('There are no more tickets!')
    elif user_age1 == 0:
        print('Zero age! Film is canceled, today we will show - YOU!')
