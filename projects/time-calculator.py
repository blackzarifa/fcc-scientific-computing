WEEKDAYS = {
    0: 'sunday',
    1: 'monday',
    2: 'tuesday',
    3: 'wednesday',
    4: 'thursday',
    5: 'friday',
    6: 'saturday',
}


def add_time(start, duration, day=''):
    # Day value
    day_number = 0
    if day != '':
        day_number = next(
            key for key, value in WEEKDAYS.items() if value == day.lower()
        )

    # Arrays
    colon_index = start.index(':')
    start_arr = [
        int(start[0:colon_index]),
        int(start[colon_index + 1 : -3]),
        start[-2:],
    ]
    duration_arr = [int(duration[0 : duration.index(':')]), int(duration[-2:])]

    # Minutes
    new_hours = 0
    new_minutes = start_arr[1] + duration_arr[1]
    if new_minutes >= 60:
        new_minutes = new_minutes - 60
        new_hours += 1

    # Hours
    new_hours += (start_arr[0] if start_arr[0] != 12 else 0) + duration_arr[0]
    extra_periods = 0
    if new_hours >= 12:
        extra_periods = new_hours // 12
        new_hours -= extra_periods * 12
        if new_hours == 0:
            new_hours = 12

    # Period
    is_am_original = start_arr[2] == 'AM'
    is_am = is_am_original
    if extra_periods % 2:
        is_am = not is_am
    new_period = 'AM' if is_am else 'PM'

    # Count days
    extra_days = extra_periods // 2
    if not is_am_original and extra_periods % 2 == 1:
        extra_days += 1

    days_str = ''
    if extra_days == 1:
        days_str = '(next day)'
    elif extra_days > 1:
        days_str = f'({extra_days} days later)'

    # Count Weekday
    day_number += extra_days
    new_day = ''
    if day != '':
        new_day = WEEKDAYS[day_number % 7].capitalize()
        return f'{new_hours}:{new_minutes} {new_period}, {new_day} {days_str}'

    return f'{new_hours}:{new_minutes} {new_period} {days_str}'


if __name__ == '__main__':
    print(add_time('11:00 PM', '1:00'))
    print(add_time('12:00 PM', '12:00', 'tuesday'))
    print(add_time('12:00 PM', '2:00'))
