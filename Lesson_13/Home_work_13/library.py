import requests
from datetime import date
from prettytable import PrettyTable

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"


def get_json_requests():
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

    return response.json()


def write_data_to_file(data):
    my_table = PrettyTable()
    my_table.field_names = ["Currency", "To Currency", "Rate"]
    my_table.align["Currency"] = "l"
    my_table.align["Rate"] = "r"

    for currency in data:
        currency_name = currency["txt"]
        currency_rate = currency["rate"]
        to_currency = "to UAH"
        my_table.add_row([currency_name, to_currency, currency_rate])

    with open("exchange_rates.txt", "w", encoding="cp1251") as file:
        file.write(f"Exchange Rates on {date.today()}:\n")
        file.write(str(my_table.get_string(fields=["Currency", "To Currency", "Rate"])))


response_data = get_json_requests()
if response_data:
    write_data_to_file(response_data)
