import random


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



print(f"Множина з 6 чисел у діапазоні від 1 до 49: {get_numbers_ticket(1, 49, 6)} ")
print(f"Множина з 5 чисел у діапазоні від 1 до 36: {get_numbers_ticket(1, 36, 5)} ")