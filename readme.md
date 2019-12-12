**utils.py**

Файл содержит вспомогательные функции:
 - `logfile(string, to_catalog, filename='report.log')`:
  - `string` - строка для записи в лог-файл
  - `to_catalog` - путь до каталога где лежит лог-файл
  - `filename` - имя файла лога

Если файла нет, функция создаст его
Если файл на месте, допишет в конец

 - `tlg_msg(message)`:
  - `message` - текстовое сообщение для отправки к чат Телеги

**birthday.txt**

Файл с датами рождений и ФИО
Данные располагаются построчно и раздлены табом

**reminder.py**

Основной файл, содержит функцию `get_msg(path)`:
 - `path` - путь до файла birthday.txt

**Результат, возвращаемый `get_msg()`**

Ближайщие праздники
13-12 др у тест сегодня осталось 0 дней
16-12 др у тест 3 осталось 3 дней
20-12 др у тест 7 осталось 7 дней
