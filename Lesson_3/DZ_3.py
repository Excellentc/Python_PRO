"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о" (враховуються як великі так
і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "о"."""

while True:
    input_word = input("Input one word witch have letter \'o\', please: ")
    find_letter = input_word.lower().count("o")
    if not input_word.isalpha() or find_letter == 0:
        print("\033[31m Please, make you input again. Something wrong\033[0m")
        continue
    # count_letter_o = input_word.lower().count("o")
    print(f"Thank you, input correct.\nThere are only \033[31m{find_letter}\033[0m "
          f"letters \'O\' in the word \'{input_word} \'")
    break

"""Є list з даними 
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Зауважте, що lst1 не є статичним і може формуватися динамічно від запуску до запуску."""

list_input = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list_of_strings = []
for index in list_input:
    if type(index) == str:
        list_of_strings.append(index)
print("From list:\n", list_input)
print("All string variables\n", list_of_strings)

"""Є стрінг з певним текстом (можна скористатися input або константою). Напишіть код, який визначить кількість слів в
цьому тексті, які закінчуються на "о" (враховуються як великі так і маленькі)."""

while True:
    input_string = str(input("\033[32m Input some text, please.\n And I try to count how many words "
                             "is end to letter \'O\' or \'o\' \033[0m\n"
                             " Your input: "))
    del_space = input_string.strip()
    if del_space == "":
        print("\033[31m Please, make you input again. Something wrong\033[0m")
        continue
    break
list_split = del_space.lower().split(" ")
count_o = 0
for index in list_split:
    len_word = len(index) - 1
    if index[len_word] == "o":
        count_o += 1
print(f" Just {count_o} words ended to \'O\'") if count_o > 0 else print(" There are no words that end in \'o\'")
