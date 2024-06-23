import random


def generate_random_times(count: int, unique: bool = True):

    times = []

    while len(times) < count:
        hour = random.randint(0, 12)
        minute = random.randint(0, 59)
        time = (hour, minute)
        if unique:
            if time not in times:
                times.append(time)
        else:
            times.append(time)

        yield time
