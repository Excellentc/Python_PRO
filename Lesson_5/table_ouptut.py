from prettytable import PrettyTable
import prettytable as PR
from pprint import pprint
import random


def all_data_from_table(students_base):

    value_list = []
    names_tab = ["Name"]
    for name_student, student_info_blok in students_base.items():
        value_list.append(name_student)
        for field_name, field_data in student_info_blok.items():
            value_list.append(field_data)
            if field_name not in names_tab:
                names_tab.append(field_name)

    numbers_of_columns = len(names_tab)
    main_table = PrettyTable(names_tab)

    while value_list:
        main_table.add_row(value_list[:numbers_of_columns])
        value_list = value_list[numbers_of_columns:]
        for name_col in names_tab:
            main_table.align[name_col] = "l"
    print(main_table)

    print(main_table.get_string(sortby = "Середній бал",reversesort = True) )



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

student_score = []
for student_name, student_info_blok in student.items():
    for field_name, field_data in student_info_blok.items():
        if field_name == "Середній бал":
            student_score.append(field_data)
awg_student_score = round(sum(student_score)/len(student_score), 2)

good_student = {}
for student_name, student_info_blok in student.items():
    for field_name, field_data in student_info_blok.items():
        if field_name == "Середній бал" and field_data > 90:
            good_student[student_name] = field_data

for student_name, student_info_blok in student.items():
    if student[student_name]["Номер телефону"] is None:
        x = "+380" + str(random.randint(0, 900000000))
        student[student_name]["Номер телефону батькiв"] = x
    else:
        student[student_name]["Номер телефону батькiв"] = None

print(f"\33[32m Average score of all students \33[0m: {awg_student_score}")
print(f"\33[32m Students which have average score > 90 :\33[0m ", end=" ")
print(good_student)

while True:
    answer = str(input("\33[32m Did you want \'Table output\' for students base?\33[0m \33[34m y or n \33[0m"))
    if answer == "y" or answer == "Y" or answer == "Yes" or answer == "yes":
        all_data_from_table(student)
        break
    else:
        print(f"\33[34m Updated students database by parent's phon:\33[0m ")
        pprint(student, width=30)
        break
