from datetime import datetime


def get_days_from_today(date):
    try:
        # Рядок у дату
        input_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Поточна дату
        today = datetime.today().date()

        # Різниця в днях
        days_different = (today - input_date).days

        return days_different

    except ValueError:
        return "Помилка: введіть у форматі РРРР-ММ-ДД"



print(get_days_from_today("2026-07-23"))
print(get_days_from_today("2025-01-01"))
print(get_days_from_today("05-04-2026"))
