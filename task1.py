from datetime import datetime
import random

# Task 1
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


# Task 2
def get_numbers_ticket(min, max, quantity) -> set :
    
    #Перевірка вхідних даних
    if min < 1 or max > 1000 or quantity >= (max - min + 1) or quantity < 1:
        return []

    # Ініціалізація множини
    resulted_set = set()

    # Заповнюємо множину випадковими числами 
    # доки число унікальних не буде дорівнювати бажаній кількості 
    # але бачу, що був ще такий вариант: 
    # numbers = random.sample(range(min_num, max_num + 1), quantity)
    while len(resulted_set) < quantity:
        resulted_set.add(random.randint(min, max))

    #Повертаємо відсортировану множину
    return (sorted(resulted_set))

# Task 3
def normalize_phone(phone_number) :
    pass



# Task 1
# Запуск функції з введенням користувача
get_days_from_today(input("Введіть дату у форматі 'РРРР-ММ-ДД': "))


# Task 2
print(f"Множина з 6 чисел у діапазоні від 1 до 49: {get_numbers_ticket(1, 49, 6)} ")
print(f"Множина з 5 чисел у діапазоні від 1 до 36: {get_numbers_ticket(1, 36, 5)} ")


# Task 3
normalize_phone(input("Введіть номер телефону:"))