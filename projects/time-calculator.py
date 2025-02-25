def add_time(start, duration):
    colon_index = start.index(':')
    start_arr = [
        int(start[0:colon_index]),
        int(start[colon_index + 1 : -3]),
        start[-2:],
    ]
    duration_arr = [int(duration[0 : duration.index(':')]), int(duration[-2:])]

    new_hours = 0
    new_minutes = start_arr[1] + duration_arr[1]
    if new_minutes >= 60:
        new_minutes = new_minutes - 60
        new_hours += 1

    new_time = [new_hours, new_minutes]
    return new_time


if __name__ == '__main__':
    print(add_time('10:31 PM', '3:59'))
