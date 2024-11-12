import pandas
import numpy as np
import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import random

"""r = requests.get('https://api.github.com/events')
r1 = requests.post('https://httpbin.org/post', data={'key': 'value'})
payload = {'key1': 'value1', 'key2': 'value2'}
r2 = requests.get('https://httpbin.org/get', params=payload)
print(r2.url) # создание URL-адреса с помощью ключ-значения payload (без повторений)
print(r2.text) # так же есть возможность прочесть ответ сервера
r3 = r2.content
filename = 'exper.txt'
r4 = requests.get('https://api.github.com/events', stream=True)
print(r4.raw)
print(r4.raw.read(10))
with open(filename, 'wb') as fd:
    for chunk in r2.iter_content(chunk_size=128):
        fd.write(chunk)
"""# библиотека requests которая упрощает получение и отправку запросов

"""list_1 = [1, 2, 3, 5, 6, 1, 3, 10, 1]
s1 = pd.Series(list_1) # создание массива путем передачи значений (по умолчанию)
print(s1)
print()
dates = pd.date_range('20241112', periods=10) # создание массива с датой и повторениями с увеличением на единицу(по умолчанию)
print(dates)
print()
dates_f = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list("ABCD")) # создание массива, который бы имел рандомный набор чисел в каждом из именнованых столбцов
print(dates_f)
print()
dates_f2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20241112"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
) # так же возможно присвоить каждому столбцу отличный от других тип данных
print(dates_f2)
print()
print(dates_f2.dtypes)
"""

"""list_1 = [1, 2, 3, 5, 6, 1, 3, 10, 1]
list_2 = [5, 4, 2, 1, 3, 5, 8, 11, 53]
a1 = np.array([list_1, list_2])
print(a1.shape) # выводит количество элементов массива, то есть 2 и количество элементов из которых состоят элементы массива, то есть по 9
list_3 = np.array(list_2)
list_3[0] = 10 # numpy можно так же обращаться по индексу, чтобы менять их значения
print(list_3)
print(list_3.ndim) # ndim показывает количество отдельных пространств массива
print(list_3.size) # size показывает общее количество элементов в массиве
# так же есть zeros, которая заполняет массив нулями,
# ones, соответственно единицами,
# arange - создает определенное количество элементов начиная с нуля, если задано только количество элементов
"""