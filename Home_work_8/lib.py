
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


if __name__ == '__main__':

    seasons(data_for_check="11.11")
