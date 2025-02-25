def add_time(start, duration):
    colon_index = start.index(':')
    start_arr = [start[0:colon_index], start[colon_index + 1 : -3], start[-2:]]
    duration_arr = [duration[0 : duration.index(':')], duration[-2:]]

    new_time = duration_arr
    return new_time


if __name__ == '__main__':
    print(add_time('10:27 PM', '3:30'))
