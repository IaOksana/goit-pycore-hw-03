from datetime import datetime

def get_days_from_today(another_date_str : str) :
    # Перетворення рядка у дату
    try :
        another_date = datetime.strptime(another_date_str, '%Y-%m-%d')
    except ValueError :
        if input("Неправильний формат даних. Натисніть '+' якщо хочете спробувати ще") == "+" :
            get_days_from_today(input("Введіть дату у форматі 'РРРР-ММ-ДД': ")) 
        return
    
    # Поточна дата
    current_date = datetime.now()

    # Розрахунок кількості днів
    days_since = (current_date - another_date).days

    print(f"Різниця у днях: {days_since}")


# Запуск функції з введенням користувача
get_days_from_today(input("Введіть дату у форматі 'РРРР-ММ-ДД': "))