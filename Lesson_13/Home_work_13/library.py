import requests
from datetime import date

url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"

try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)
else:
    response_data = response.json()

    with open("exchange_rates.txt", "w", encoding="cp1251") as f:
        f.write(f"Exchange Rates on {date.today()}:\n\n")
        for currency in response_data:
            currency_name = currency["txt"]
            currency_rate = currency["rate"]
            f.write(f"{currency_name} to UAH: {currency_rate}\n")
