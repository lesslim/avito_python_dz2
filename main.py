import csv
import sys

csv_name = 'funcs_homework_employees_sample.csv'


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
    Make paths.
    """
    dep_set = set()
    with open(csv_name, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        next(data)
        for row in data:
            if row[2] not in dep_set:
                dep_set.add(row[2])
    return dep_set


def print_departments():
    """
    Print all departments.
    """
    print('\n'.join([beautify_department(i) for i in make_departments()]))


def report_department() -> dict:
    """
    Make report info.
    """
    csv_dict = dict.fromkeys(make_departments(), [])
    with open(csv_name, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=';')
        next(data)
        for row in data:
            if not csv_dict[row[2]]:
                csv_dict[row[2]] = [0, -1, 0, 0, 0]
            salary = float(row[4])
            csv_dict[row[2]][0] += 1
            if salary < csv_dict[row[2]][1] or csv_dict[row[2]][1] == -1:
                csv_dict[row[2]][1] = salary
            if salary > csv_dict[row[2]][2]:
                csv_dict[row[2]][2] = salary
            csv_dict[row[2]][4] += salary
            csv_dict[row[2]][3] = csv_dict[row[2]][4] / csv_dict[row[2]][0]
    return csv_dict


def print_report():
    """
    Print report to the console.
    """
    print("Название отдела;Численность;Вилка;Средняя зарплата")
    dep = report_department()
    for i in dep:
        print(beautify_department(i), dep[i][0],
              f'{dep[i][1]} - {dep[i][2]}', round(dep[i][3], 2), sep=';')


def report_department_to_csv():
    """
    Output the report to csv.
    """
    with open('report.csv', 'w') as f:
        sys.stdout = f
        print_report()


def choose_option():
    """
    Getting the option number from the user.
    """
    print(
        """
    Доступны следующие опции:
    1. Вывести все отделы
    2. Вывести в консоль сводный отчёт по отделам: название, численность, вилка зарплат, средняя
    3. Сохранить сводный отчёт (см. п.2) в виде csv-файла.
        """
    )
    option = ''
    options = {'1': print_departments, '2': print_report,
               '3': report_department_to_csv}
    while option not in options:
        print('Введите {} / {} / {}'.format(*options), "")
        option = input()
    options[option]()


if __name__ == "__main__":
    choose_option()
