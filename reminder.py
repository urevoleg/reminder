import re
import datetime
import pandas as pd
from utils import *

# файл с датами др и именами людей
birthday = 'birthday.txt'

def get_msg(path=birthday):
    try:

        # разбираем файл со списком
        # who - у кого др
        # when - когда др
        # читаем файл с др
        dates = pd.read_csv(path, header=None, names=['when', 'who'], sep='\t', encoding='cp1251')

        # создаем даты сегодня/через 3 дня/через 7 дней
        # сразу после создания ищем нужные нам даты и добавляем их с словарь
        msg_dict, msg = {}, ""
        for days_delta in [0, 3, 7]:
            # заполняем столбец d_X своей датой
            dates[f'd_{days_delta}'] = [(datetime.datetime.now() + datetime.timedelta(days=days_delta)).strftime('%d-%m')
                                        for _ in range(dates.shape[0])]
            # ищем пересечение нужных дат
            target = dates[dates['when'] == dates[f'd_{days_delta}']][['when', 'who']]

            # заполняем сообщение
            # проверяем если поиск не пустой
            if not target.empty:
                msg += target['when'].values[0] + ' др у ' + target['who'].values[0] + f' осталось {days_delta} дней\n'

        if msg != "":
            return 'Ближайщие праздники\n' + msg
        else:
            return msg
    except Exception as e:
        #logfile(string = str(e))
        print(str(e))

"""
Вызов функции
"""

if __name__ == '__main__':
    msg = get_msg()
    if msg:
        print(msg)
        tlg_msg(msg)