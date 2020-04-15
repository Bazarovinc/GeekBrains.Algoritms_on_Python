"""1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для каждого
    предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
    наименования предприятий, чья прибыль выше среднего и ниже среднего."""

from collections import namedtuple

"""В данной задачи разрешается, как я понял использование приведения к типу"""

company = namedtuple('company', 'company_name, profit')
n = int(input("Введите колличество компаний: "))
list_of_companies = []
for i in range(n):
    name = input("Введите наименование компании: ")
    p = []
    for j in range(4):
        p.append(int(input(f"Введите прибыль за {j + 1} квартал: ")))
    list_of_companies.append(company(name, sum(p)))
mid = 0
for i in list_of_companies:
    mid += i.profit
mid /= n
print(f"Компании, чья прибыль за год выше среднего({mid}):")
for i in list_of_companies:
    if i.profit > mid:
        print(f'{i.company_name} - {i.profit}')
print(f"Компании, чья прибыль за год ниже среднего({mid}):")
for i in list_of_companies:
    if i.profit < mid:
        print(f'{i.company_name} - {i.profit}')
