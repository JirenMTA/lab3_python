from termcolor import colored
from random import choice


def print_menu():
    print("""Choose an option:
    1. Get data from file valid data.
    2. Sort list by height.
    3. Sort list by work experience
    4. Sort list by passport number
    5. Save sorted data to new file
    6. Check data
    """, end='')


# сотировка слиянием
def merge_sort(arr_list, field, start, end):
    """Sorts the list from indexes start to end - 1 inclusive."""
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(arr_list, field, start, mid)
        merge_sort(arr_list, field, mid, end)
        merge_list(arr_list, field, start, mid, end)


def merge_list(arr_list, field, start, mid, end):
    left = arr_list[start:mid]
    right = arr_list[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if float(left[i][field]) <= float(right[j][field]):
            arr_list[k] = left[i]
            i = i + 1
        else:
            arr_list[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            arr_list[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            arr_list[k] = right[j]
            j = j + 1
            k = k + 1


def print_check_data(arr_list):
    i = 1
    for x in range(0, 10):
        person = choice(arr_list)
        print(colored(f"---- Person {i} ----", 'green'))
        i += 1
        for key, value in person.items():
            print(f'\033[93m' + str(key) + ': ' + str(value) + '\033[0m')

