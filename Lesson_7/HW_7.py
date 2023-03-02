from typing import Union, Any

"""Напишіть функцію, яка визначає сезон за датою. Функція отримує стрінг у форматі "[день].[місяць]"
(наприклад "12.01", "30.08", "1.11" і тд) і повинна повернути стрінг з відповідним сезоном, до якого відноситься ця дата
 ("літо", "осінь", "зима", "весна")
 Напишіть докстрінг функціi
"""


def seasons(data_for_check: str) -> str:
    """
    The function takes the string data-"date" in a certain format and calculates what time of year this date belongs to.
    String argument :"date", format - "[day].[month]" e.g. "12.01"
    :param data_for_check: string
    :return: string
    """
    list_of_seasons = {"01": (31, "Зима"), "02": (28, "Зима"), "03": (31, "Весна"),
                       "04": (30, "Весна"), "05": (31, "Весна"), "06": (30, "Лето"),
                       "07": (31, "Лето"), "08": (31, "Лето"), "09": (30, "Осень"),
                       "10": (31, "Осень"), "11": (30, "Осень"), "12": (31, "Зима")}
    not_valid_data_types = ["True", "False", "None"]

    list_with_data_and_month = data_for_check.split(".")

    if list_with_data_and_month[0] in not_valid_data_types or list_with_data_and_month[1] in not_valid_data_types:
        error_message_type = 'Incorrect data type in string'
        return error_message_type

    if int(list_with_data_and_month[1]) > 12 or int(list_with_data_and_month[1]) <= 0 \
            or len(list_with_data_and_month[1]) != 2:
        error_message_month = 'Incorrect month number'
        return error_message_month

    for month, month_data in list_of_seasons.items():
        if list_with_data_and_month[1] == month:
            if int(list_with_data_and_month[0]) > month_data[0] or int(list_with_data_and_month[0]) <= 0 \
                    or len(list_with_data_and_month[0]) != 2:
                error_message_days = 'Incorrect days number'
                return error_message_days
            else:
                return month_data[1]


seasons(data_for_check="None.11")


""" Напишіть функцію "Тупий калькулятор", яка приймає два числових аргументи і строковий, який відповідає за операцію 
між ними (+ - / *). Функція повинна повертати значення відповідної операції (додавання, віднімання, ділення, множення),
інші операції не допускаються. Якщо функція оримала невірний тип данних для операції (не числа) або неприпустимий 
(невідомий) тип операції вона повинна повернути None і вивести повідомлення "Невірний тип даних" або "Операція не
 підтримується" відповідно.
 Напишіть докстрінг функціi
"""


def calculation_evaluation(first_number: Union[int, float], second_number: Union[int, float],
                           arithmetic_operation: str) -> Union[int, float]:
    """
    Function, takes three arguments as input: two numeric and one string.\n
    Depending on what mathematical operation came in the string argument, the corresponding arithmetic operation
    takes place from 4 options, between two digital arguments.\n
    String argument : one of the arithmetic operations (* / + - )\n
    Numeric argument: int or float\n
    :param first_number: int or float
    :param second_number: int or float
    :param arithmetic_operation: string
    :return: int or float
    """
    match arithmetic_operation:
        case "/":
            calculation_result = first_number / second_number
            return calculation_result
        case "+":
            calculation_result = first_number + second_number
            return calculation_result
        case "-":
            calculation_result = first_number - second_number
            return calculation_result
        case "*":
            calculation_result = first_number * second_number
            return calculation_result


def calculator(first_argument: Union[int, float], second_argument: Union[int, float], arithmetic_operation: str) -> Any:
    """
    Mini calculator for one arithmetic operations, takes three arguments as input: two numeric and one string.\n
    String argument : one of the arithmetic operations (* / + - )\n
    Numeric argument: int or float\n
    Result of function : arithmetic operation (only one from "String argument") between two numeric arguments
    In case of incorrect input of an arithmetic operation returns None or an "Error message".\n
    Error message: "Invalid data type" or "Operation not supported"\n
    :param first_argument: int or float
    :param second_argument: int or float
    :param arithmetic_operation: string
    :return: int or float
    """

    valid_arithmetic_operation = ['+', '-', '/', '*']

    if type(arithmetic_operation) != str or (type(first_argument) is bool or type(second_argument) is bool):
        print('Invalid data type')
        return None
    if arithmetic_operation not in valid_arithmetic_operation:
        print('Operation not supported')
        return None
    else:
        try:
            check_division_by_zero_and_type = first_argument / second_argument
        except ZeroDivisionError:
            error_message = "You entered incorrect numerical value. Check second number value its should be != 0"
            return error_message
        except TypeError:
            error_message = "Invalid data type. Check arguments type. "
            return error_message
        else:
            calculation_result = calculation_evaluation(first_number=first_argument, second_number=second_argument,
                                                        arithmetic_operation=arithmetic_operation)
            return calculation_result


print(calculator(first_argument=7, second_argument=4.5, arithmetic_operation="*"))
