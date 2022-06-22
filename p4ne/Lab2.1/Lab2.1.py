#!/usr/local/bin/python3

# Подключаем библиотечные функции
from matplotlib import pyplot
from openpyxl import load_workbook

# Определяем служебную функцию выделения значения из ячейки
def getvalue(x):
    return x.value


# Извлекаем таблицу MS Excel из файла в переменную
wb = load_workbook('data_analysis_lab.xlsx')

# Извлекаем лист из таблицы
sheet = wb['Data']

# Извлекаем и преобразуем три столбца из листа
years = list(map(getvalue, sheet['A'][1:]))
temperature = list(map(getvalue, sheet['C'][1:]))
activity = list(map(getvalue, sheet['D'][1:]))

# Создаём графическое представление, но пока не показываем
pyplot.plot(years, temperature)
pyplot.plot(years, activity)

# Украшаем график - добавляем надписи
pyplot.xlabel('Годы')
pyplot.ylabel('Температура/Активность Солнца')
pyplot.legend(loc='upper left')

# Отображаем график просто
pyplot.show()