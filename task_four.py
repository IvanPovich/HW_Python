from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    res = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year = today.year)

    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year = today.year + 1)

    days_to_birthday = (birthday_this_year - today).days

    if 0 <= days_to_birthday <= 7:
        if birthday_this_year.weekday() >= 5:
            birthday_this_year += timedelta(days = 7 - birthday_this_year.weekday())

    res.append({
        "name": user["name"],
        "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
        })
    
    return res

#Example
random_users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(random_users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

