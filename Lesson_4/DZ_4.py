"""Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
Напишіть код, який видалить (не створить новий, а саме видалить!) з нього всі числа, які менше 21 і більше 74."""

my_list = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]
print(f"\033[31m First version: usage del list() in end\033[0m")
print(f"\033[32m Default list :\033[0m\n{my_list}")
my_list.sort()
print(f"\033[32m Sorted list : \33[0m\n{my_list}")
end_point, start_point = 0, 0
for idx in range(len(my_list)):
    if 21 > my_list[idx]:
        start_point = idx
    elif my_list[idx] > 74:
        end_point = idx
        break
del my_list[end_point:]
del my_list[:start_point+1]
print(f"\033[32m List after checking and deleting by pattern  21 < x < 74 : \33[0m\n{my_list}")



"""Є два довільних числа які відповідають за мінімальну і максимальну ціну.
   Є Dict з назвами магазинів і цінами:
    { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245, 
 "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "roze-tka": 38.003}. 
 Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких потрапляють в діапазон між мінімальною
і максимальною ціною.
Наприклад:

lower_limit = 35.9
upper_limit = 37.339
> match: "x-store", "main-service"
"""


def filter_list(data_dict, low_limit, upp_limit):
    string_list = []
    for key, value in data_dict.items():
        if low_limit < value < upp_limit:
            string_list.append(key)
            string_list.reverse()
    return string_list


my_dict = {"cito": 47.999, "BB_studio": 42.999, "momo": 49.999, "main-service": 37.245,
           "buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "store": 37.720, "roze-tka": 38.003}

lower_limit = 35.9
upper_limit = 37.339

output_data = filter_list(my_dict, lower_limit, upper_limit)

print("\33[32m Data for filtering: \33[0m", my_dict)
print(f"\033[32m Filtration conditions: \033[34m min price - {lower_limit}, max price - {upper_limit} \033[0m")
print("\33[32m Matches on your request: \33[0m", ", ".join(output_data))

output_data = ["x-store", "main-service"]
print("\33[32m > match:\33[0m", end=" ")

for ind in range(len(output_data)):
    if ind == len(output_data) - 1:
        print(f"\33[34m\"{output_data[ind]}\"\33[0m", end="")
    else:
        print(f"\33[34m\"{output_data[ind]} \"\33[0m", end=", ")
