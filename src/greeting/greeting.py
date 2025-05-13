import datetime


def get_greeting() -> str:
    current_time = datetime.datetime.now()
    current_hour = current_time.hour
    if 5 <= current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    elif 18 <= current_hour < 22:
        return "Good evening!"
    else:
        return "Good night!"
