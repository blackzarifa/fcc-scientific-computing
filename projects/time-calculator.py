def add_time(start, duration):
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
    new_hours += start_arr[0] + duration_arr[0]
    extra_periods = 0
    if new_hours >= 12:
        extra_periods = new_hours // 12
        new_hours -= extra_periods * 12
        if new_hours == 0:
            new_hours = 12

    # Period
    is_am = start_arr[2] == 'AM'
    if extra_periods % 2:
        is_am = not is_am
    new_period = 'AM' if is_am else 'PM'

    new_time = [new_hours, new_minutes, extra_periods, new_period]
    return new_time


if __name__ == '__main__':
    print(add_time('11:00 PM', '1:00'))
    print(add_time('12:00 PM', '12:00'))
    print(add_time('12:00 PM', '2:00'))
