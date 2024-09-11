import datetime
today = datetime.date.today()
birthday_this_year = datetime.date(today.year, 7, 31)
birthday_next_year = datetime.date(today.year +1, 7, 31)
if today < birthday_this_year:
    days_left = (birthday_this_year - today).days
    print(f'Вечеринка еще впереди.Осталось {days_left} дней до дня рождения Гарри.')
elif today == birthday_this_year:
    print('С днем рождения Гарри!! Вечеринка сегодня.')
else:
    days_left = (birthday_next_year - today).days
    print(f'Вечеринка уже прошла. До следующей вечеринки {days_left} дней')

