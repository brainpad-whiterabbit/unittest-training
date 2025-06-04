import datetime


def get_greeting() -> str:
    current_time = datetime.datetime.now().time()

    if datetime.time(5, 0, 0) <= current_time < datetime.time(12, 0, 0):
        return "Good morning!"
    elif datetime.time(12, 0, 0) <= current_time < datetime.time(18, 0, 0):
        return "Good afternoon!"
    elif datetime.time(18, 0, 0) <= current_time < datetime.time(22, 0, 0):
        return "Good evening!"
    else:
        return "Good night!"
