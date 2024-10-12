from datetime import datetime, timedelta

def get_days_from_today():
    # Якась дата
    another_date = datetime(input('Введіть дату у форматі: '))

    # Поточна дата
    current_date = datetime.now()

    # Розрахунок кількості днів
    days_since = current_date.toordinal() - another_date.toordinal()

    print(days_since)


get_days_from_today()