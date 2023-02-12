"""
Напишіть функцію, яка приймає два аргументи.
- Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
- Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
- В будь-якому іншому випадку - функція повертає кортеж з двох агрументів

"""


def two_numbers(list_input):
    result_numbers = float(list_input[0]) * float(list_input[1])
    return result_numbers


def two_words(list_input):
    result_words = list_input[0] + list_input[1]
    return result_words


def olive_word_number(list_input):
    tuple_to_output = (list_input[0], list_input[1],)
    return tuple_to_output


def start_homework(list_to_check):

    if type(list_to_check[0]) == bool or type(list_to_check[1]) == bool:
        result_to_print = "Not correct input values"
    elif list_to_check[0] is None or list_to_check[1] is None:
        result_to_print = "Not correct input values"
    elif list_to_check[0].isalpha() and list_to_check[1].isalpha():
        result_to_print = two_words(list_input=list_to_check)
    else:
        try:
            list_value_1, list_value_2 = float(list_to_check[0]), float(list_to_check[1])
        except ValueError:
            result_to_print = olive_word_number(list_input=list_to_check)
        else:
            result_to_print = two_numbers(list_input=list_to_check)

    return result_to_print


two_words_two_numbers = ["one", "two"]
result = start_homework(list_to_check=two_words_two_numbers)
print(f"Values {two_words_two_numbers}", result)

two_words_two_numbers = ["2", "2.5"]
result = start_homework(list_to_check=two_words_two_numbers)
print(f"Values {two_words_two_numbers}", result)

two_words_two_numbers = [True, "2"]
result = start_homework(list_to_check=two_words_two_numbers)
print(f"Values {two_words_two_numbers}", result)

two_words_two_numbers = [None, "2"]
result = start_homework(list_to_check=two_words_two_numbers)
print(f"Values {two_words_two_numbers}", result)

two_words_two_numbers = ["23.6", "two"]
result = start_homework(list_to_check=two_words_two_numbers)
print(f"Values {two_words_two_numbers}", result)


"""Візьміть попереднє дз "Касир в кінотеатрі" і перепишіть за допомогою функцій. Памʼятайте про SRP!"""

"""Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік
  (можно використати константу або функцію input(), на екран має бути виведено лише одне повідомлення,
   також подумайте над варіантами, коли введені невірні дані).
        якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
        якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
        якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
        якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
        у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!" 
        """


# def color_output_green(sentence):
#     start_green = "\33[32m"
#     end_green = "\33[0m"
#     new_sentence = start_green + sentence + end_green
#     return new_sentence
#
#
# def color_output_red(sentence):
#     start_red = "\33[31m"
#     end_red = "\33[0m"
#     new_sentence = start_red + sentence + end_red
#     return new_sentence
#
#
# def color_output_blue(sentence):
#     start_blue = "\33[34m"
#     end_blue = "\33[0m"
#     new_sentence = start_blue + sentence + end_blue
#     return new_sentence
#
#
# def check_luck(user_input_str):
#     if user_input_str.find('7') >= 0:
#         lucky_sentence = 'You are will be lucky today!'
#         lucky_guy_msg = color_output_blue(sentence=lucky_sentence)
#     else:
#         lucky_guy_msg = ''
#     return lucky_guy_msg
#
#
# def check_user_age(user_input_int, check__lucky):
#     lucky_or_not = check_luck(user_input_str=check__lucky)
#     output_message = ""
#     if 0 < user_input_int < 7:
#         output_message = 'Where are your parents? '
#     elif 7 <= user_input_int < 16:
#         output_message = "This is an adult movie! " + lucky_or_not
#     elif 16 <= user_input_int <= 65:
#         output_message = "There are no more tickets! " + lucky_or_not
#     elif 65 < user_input_int < 105:
#         output_message = "Show your pension certificate! " + lucky_or_not
#     elif user_input_int == 0 or user_input_int >= 105:
#         negative_value = "Liar. People Don't live with this age "
#         output_message_color = color_output_red(sentence=negative_value)
#         return output_message_color
#     output_message_color = color_output_green(sentence=output_message)
#     return output_message_color
#
#
# def start_homework():
#     while True:
#         try:
#             user_input = input("\33[32mInput your age, only numbers please: \33[0m")
#             user_input_int_ = abs(int(user_input))
#         except ValueError:
#             bad_attempt = color_output_red("Wrong input. Let's do this again")
#             print(bad_attempt)
#         else:
#             print(f"\33[32mGood input\33[0m You age is : {user_input_int_}")
#             result_to_print = check_user_age(user_input_int=user_input_int_, check__lucky=user_input)
#             print(result_to_print)
#             print()
#             new_attempt = input("Want to repeat this ? Input Yes ")
#             if new_attempt == 'Yes' or new_attempt == 'yes' or new_attempt == 'y' or new_attempt == 'Y':
#                 continue
#             print("By")
#             break
#
#
# start_homework()
