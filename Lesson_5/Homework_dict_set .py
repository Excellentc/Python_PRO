"""
Завдання 1
Макс 40 балів
написати програму, яка просить в користувача ввести через пробіл міста, в яких він був за минулі 10 років
потім окремо запросити у користувача міста, куди він хоче поїхати внаступні 10 років
вивести на екран повідомлення з текстом про те, що користувачу, мабуть, дуже сподобалося в містах, які він повторив в
двох циклах вводу, а саме... (сформувати строку, використовуючи join)
якщо повтору не було - вивести повідомлення, що користувач відкритий до чогось нового

врахувати випадки, що користувач нічого не вводить не потрібно, в даному випадку вам явно зазначено,
що ці перевірки не потрібні.
не потрібно перевіряти введення цифр
ми виходим із того, що користувач введе щось на зразок "Київ Тернопіль париЖ акапулько-80"

В той же час врахуйте, що користувач може вводити дані в різних регістрах

використати сети!!!
"""
# Data -  for automatically input lists of cities
# cities_was_input = "киев Харьков львов ОДЕССА Париж париж парИж"
# cities_was_not_input = "Копенгаген  Днепр Харьков Малая_Прихватка Конские_Раздоры паРиж "

cities_was_input = input("Enter cities where you have been for 10 years (through a space)")
cities_was_set = set(list(cities_was_input.title().split(" ")))

cities_was_not_input = input("Enter cities which you want to visit in next 10 years (through a space)")
cities_was_not_set = set(list(cities_was_not_input.title().split(" ")))

match_cities = cities_was_set.intersection(cities_was_not_set)
if len(match_cities) > 0:
    print("\33[32m Apparently, you liked the cities - \33[0m"+", ".join(match_cities) +
          "\33[32m , since you want to visit there again\33[0m")
else:
    print("\33[32m You have been to many places, but there is still half the world left\33[0m")

"""Завдання 2
макс 60 балів
зауважте, що значення, що зберігається в кожному елементі - теж словник, і доступ до вкладеного списку
здійснюється за механізмом
student[outer_dict_key][inner_dict_key]

Є дані студентів (комбінація імені та прізвища унікальна), що зберігаються за допомогою словника
1 - програмно добавити одного студента, з заповненням усіх полів (вік - від 18 до 40, цілочисельне значення,
    бал від 0 до 100 (інт чи флоат)
2 - створити і вивести на екран список студентів (імя та прізвище та середній бал), у яких середній бал більше 90
    сам формат наповнення цього списку up to you
3 - визначити середній бал по групі
4 - при відсутності номеру телефону у студента записати номер батьків (номер на ваш вибір)

не забувайте виводити інформаційні повідомлення щодо інформації, яку ви виводите
"""
from pprint import pprint
import random

student = {
    'Іван Петров': {
        'Пошта': 'Ivan@gmail.com',
        'Вік': 14,
        'Номер телефону': '+380987771221',
        'Середній бал': 95.8
    },
    'Женя Курич': {
        'Пошта': 'Geka@gmail.com',
        'Вік': 16,
        'Номер телефону': None,
        'Середній бал': 64.5
    },
    'Маша Кера': {
        'Пошта': 'Masha@gmail.com',
        'Вік': 18,
        'Номер телефону': '+380986671221',
        'Середній бал': 80
    },
}

new_student_data = {
    'Пошта': 'serg_1@gmail.com',
    'Вік': 22,
    'Номер телефону': None,
    'Середній бал': 96.4
    }
student["Сергей Куч"] = new_student_data

# calculate the average score of students
student_score = [value1 for key, value in student.items() for key1, value1 in value.items() if key1 == "Середній бал"]
awg_student_score = round(sum(student_score)/len(student_score), 2)

# filter students by maximum score> 90
good_student = {key: value1 for key, value in student.items() for key1, value1 in value.items()
                if key1 == "Середній бал" and value1 > 90}

# added parents phon
for key, value in student.items():
    if student[key]["Номер телефону"] is None:
        x = "+380" + str(random.randint(0, 900000000))
        student[key]["Номер телефону батькiв"] = x

print(f"\33[32m Average score of all students \33[0m: {awg_student_score}")
print(f"\33[32m Students which have average score > 90 :\33[0m ", end=" ")
print(good_student)
print(f"\33[34m Updated students database by parent's phon:\33[0m ")
pprint(student, width=30)
