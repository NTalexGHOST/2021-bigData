import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./flavors_of_cacao.csv', header=0)
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True)


def possibilities(info, condition):
    df = info.query(condition)
    info = info.groupby('Company Location')
    df = df.groupby('Company Location')
    return df['Rating'].count() / info['Rating'].count()


# Посчитать априорные вероятности для каждой страны происхождения (Company Location) получения оценки выше 3.1

temp = possibilities(data, 'Rating > 3.1').dropna()
print('----- №1 Вероятность получения оценки выше 3.1 -----')
print(temp)

# Используя их, посчитать вероятность того, что новый сорт какао с содержанием выше 73% (Cocoa Percent)
# будет иметь оценку выше 3.1 для стран b) северного полушария



# Сделать прогноз, какова вероятность того, что обзоры какао после 2014 года будут иметь оценку выше медианной
# по всему периоду после 2010 года.


