from datetime import datetime, timedelta


def get_upcoming_birthdays(users) -> list :
    
    users_to_congrat = []
    
    today = datetime.today().date()

    try :
        for user in users:
            
            user_birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date() 
            
            # Empoyee's birthday this year
            user_birthday = user_birthday.replace(year=today.year)
            
            # NewYear case
            if (user_birthday < today) : 
                user_birthday = user_birthday.replace(year=today.year + 1)

            # How many days before birthday
            days_before = (user_birthday - today).days
            
            # If current week
            if (0<= days_before <= 7) :
                # If on weekends 
                if (user_birthday.weekday() >=5) :
                    user_birthday += timedelta(days=(7 -user_birthday.weekday()))

                users_to_congrat.append({"name" : user["name"], "congratulation date" : user_birthday.strftime("%Y.%m.%d")})
            
    except:
        print("Error")

    return (users_to_congrat)


users = [
    {"name": "John Doe", "birthday": "1985.10.13"},
    {"name": "Jane Smith", "birthday": "1990.10.16"}
]

print(f"Список привітань на цьому тижні: {get_upcoming_birthdays(users)} ")