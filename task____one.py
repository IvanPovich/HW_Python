from datetime import datetime

def get_days_from_today(date: str) -> int:
    input_date = datetime.strptime(date, '%Y-%m-%d').date()

    today = datetime.today().date()

    delta = today - input_date

    return delta.days

#Example

random_date = '2022-04-15'

day_dif = get_days_from_today(random_date)
print(day_dif)


