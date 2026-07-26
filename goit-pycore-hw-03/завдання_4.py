from datetime import datetime, date, timedelta


def get_upcoming_birthdays(users):
    today = date.today()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # В цьому році
        birthday_this_year = birthday.replace(year=today.year)

        # Вже минув, тоді наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        days_left = (birthday_this_year - today).days

        # Протягом наступних 7 днів
        if 0 <= days_left <= 7:
            congratulation_date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)

            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return result


users = [
    {"name": "ALIMA", "birthday": "2004.05.23"},
    {"name": "MARIA", "birthday": "1995.01.27"},
    {"name": "OLENA", "birthday": "2000.12.31"}
]

print(get_upcoming_birthdays(users))