from package_console.lab2 import lab2_app
from package_console.lab3 import print_menu
from package_console.lab3 import merge_sort
from package_console.lab3 import print_check_data
from termcolor import colored
import json
# Пользовать пртложение из 2 лабораторной работы
lab2_app()

# Реализовать консольное приложение для сопротивления
data = []
while True:
    print_menu()
    solution = int(input())
    if solution == 1:
        print("Input file data: ", end='')
        file_name = input()
        with open(file_name, 'r', encoding='windows-1251') as fh:
            data = json.load(fh)
        print(colored(f'Got data from file: {file_name}', 'blue'))
    elif solution == 2:
        merge_sort(data, 'height', 0, len(data))
        print(colored("Data sorted by height", 'blue'))
    elif solution == 3:
        merge_sort(data, 'work_experience', 0, len(data))
        print(colored("Data sorted by work experience", 'blue'))
    elif solution == 4:
        merge_sort(data, 'passport_number', 0, len(data))
        print(colored("Data sorted by passport number", 'blue'))
    elif solution == 5:
        print("Enter file name: ", end='  ')
        sorted_file = input()
        with open(sorted_file, 'w', encoding='windows-1251') as fh:
            beauty_data = json.dumps(data, ensure_ascii=False, indent=4)
            fh.write(beauty_data)
        print(colored(f"Sorted data saved in {sorted_file}", 'blue'))
    elif solution == 6:
        print_check_data(data)
    else:
        print("Exit menu!")
        break
