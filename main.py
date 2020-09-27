import csv
from typing import List


csvname = 'funcs_homework_employees_sample.csv'

def beautify_department(dep: str) -> str:
    """
    Make department (with comment) from path.
    """
    delimeter = ' -> '
    ind = dep.rfind(delimeter)
    if ind == -1:
        return dep
    return ''.join([dep[ind + len(delimeter):], " (", dep[:ind], ")"])


def make_departments() -> set:
    """

    :return:
    """
    dep_set = set()
    with open(csvname, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        for row in data:
            if row[2] not in dep_set:
                dep_set.add(row[2])
    return dep_set
    # return [beautify_department(i) for i in dep_set]


def print_departments():
    """

    :return:
    """
    print('\n'.join([beautify_department(i) for i in make_departments()]))


def report_department() -> list:
    """

    :return:
    """
    csv_list = []
    for i in make_departments():

    return csv_list


def print_report():
    """

    :return:
    """
    pass


def report_department_to_csv():
    """

    :return:
    """
    # print("sfvdf")
    pass


def choose_option():
    """
    Getting the option number from the user.
    """
    print(
        """
        Доступны следующие опции:
        1. Вывести все отделы
        2. Вывести в консоль сводный отчёт по отделам: название, численность, "вилка" зарплат, средняя зарплата
        3. Сохранить сводный отчёт (см. п.2) в виде csv-файла.
        """
    )
    option = ''
    options = {'1': print_departments, '2': print_report, '3': report_department_to_csv}
    while option not in options:
        print('Введите {} / {} / {}'.format(*options), "")
        option = input()
    # print(options[option])
    options[option]()


if __name__ == "__main__":
    choose_option()
