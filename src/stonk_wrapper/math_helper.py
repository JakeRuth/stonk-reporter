def format_number(string_float):
    if (string_float == 'None'):
        print('WARNING: Unexpected None value for column, defaulting to 0')
        return 0

    return round(float(string_float), 2) / 1000

def calc_percent_increase(current, previous):
    if current <= 0 or previous <= 0:
        return 0
    increase = (current - previous) / previous
    return round(increase * 100, 2)
