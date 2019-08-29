
# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего

from collections import namedtuple

Company = namedtuple('Company', 'name, profit')

k = int(input('Введите кол-во предприятий: '))

comp = []
for i in range(1, k+1):
    c = Company(input('Введите название: '), float(input('Введите прибыль: ')))
    comp.append(c)

sum_profit = 0

for i, items in enumerate(comp):
    sum_profit += items.profit
sr_profit = sum_profit/k

print(f'\nСреднее значение прибыли: {sr:.1f}')

lst_more = []
lst_less = []

for i, items in enumerate(comp):
    if items.profit < sr_profit:
        lst_less.append(items.name)
    else:
        lst_more.append(items.name)

print('Компании, прибыль которых меньше среднего:', lst_less)
print('Компании, прибыль которых больше среднего:', lst_more)
