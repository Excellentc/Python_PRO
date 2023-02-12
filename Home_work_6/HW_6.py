"""
Напишіть функцію, яка приймає два аргументи.
- Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
- Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
- В будь-якому іншому випадку - функція повертає кортеж з двох агрументів

"""


def multiplication_of_two_arguments(value_one_check, value_two_check):
    result_numbers = value_one_check * value_two_check
    return result_numbers


def joining_two_words(value_one_check, value_two_check):
    result_words = value_one_check + value_two_check
    return result_words


def creating_a_tuple_with_data_matching_the_third_condition(value_one_check, value_two_check):
    tuple_to_output = (value_one_check, value_two_check,)
    return tuple_to_output


def start_homework(value_one, value_two):

    if (type(value_one) == int or type(value_one) == float) and (type(value_two) == int or type(value_two) == float):
        result_to_print = multiplication_of_two_arguments(value_one_check=value_one, value_two_check=value_two)
    else:
        try:
            list_value_1, list_value_2 = value_one.isalpha(), value_two.isalpha()
            result_to_print = joining_two_words(value_one_check=value_one, value_two_check=value_two)
        except AttributeError:
            result_to_print = creating_a_tuple_with_data_matching_the_third_condition(value_one_check=value_one,
                                                                                      value_two_check=value_two)
    pass


start_homework(5, 5)


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


def color_output(sentence, color):
    start_color = "\33["+color+"m"
    end_color = "\33[0m"
    new_sentence = start_color + sentence + end_color
    return new_sentence


def check_luck(user_input_str):
    if user_input_str.find('7') >= 0:
        lucky_sentence = 'You are will be lucky today!'
        lucky_guy_msg = color_output(sentence=lucky_sentence, color="34")
    else:
        lucky_guy_msg = ''
    return lucky_guy_msg


def check_user_age(user_input_int, check__lucky):
    lucky_or_not = check_luck(user_input_str=check__lucky)
    output_message = ""
    if 0 < user_input_int < 7:
        output_message = 'Where are your parents? '
    elif 7 <= user_input_int < 16:
        output_message = "This is an adult movie! " + lucky_or_not
    elif 16 <= user_input_int <= 65:
        output_message = "There are no more tickets! " + lucky_or_not
    elif 65 < user_input_int < 105:
        output_message = "Show your pension certificate! " + lucky_or_not
    elif user_input_int == 0 or user_input_int >= 105:
        negative_value = "Liar. People Don't live with this age "
        output_message_color = color_output(sentence=negative_value, color="31")
        return output_message_color
    output_message_color = color_output(sentence=output_message, color="32")
    return output_message_color


def start_homework():
    while True:
        try:
            data_entry_suggestion = "Input your age, only numbers please: "
            user_input = input(color_output(sentence=data_entry_suggestion, color="32"))
            user_input_int_ = abs(int(user_input))
        except ValueError:
            bad_attempt = color_output("Wrong input. Let's do this again", color="31")
            print(bad_attempt)
        else:
            successful_input = "Good input: "
            output_successful_input = color_output(sentence=successful_input, color="32")
            print(output_successful_input, f"You age is : {user_input_int_}")
            result_to_print = check_user_age(user_input_int=user_input_int_, check__lucky=user_input)
            print(result_to_print, end="\n\n")
            new_attempt = input("Want to repeat this ? Input Yes ")
            if new_attempt == 'Yes' or new_attempt == 'yes' or new_attempt == 'y' or new_attempt == 'Y':
                continue
            print("By")
            break


start_homework()
