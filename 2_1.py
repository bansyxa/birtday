import datetime
today = datetime.date.today()
birthday = datetime.date(today.year, 7, 31)
if today < birthday:
    days_left = (birthday - today).days
    print(f'Вечеринка еще впереди. Осталось {days_left} дней до дня рождения Гарри.')
elif today == birthday:
    print('С днем рождения, Гарри.Вечеринка сегодня!')
else:
    print('День рождения уже прошел')