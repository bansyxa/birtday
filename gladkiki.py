import datetime
try:
    today = datetime.date.today()
    if today.month == 7 and today.day == 31:
        print('C днем рождения,Гарри!Вечеринка сегодня')
    else:
        print('Cегодня не день рождения Гарри')
except ValueError as e:
    print('Некорректный формат даты')