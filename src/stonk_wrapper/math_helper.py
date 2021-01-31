def format_number(input):
    number = string_to_float(input)
    if number == 0:
        return number
    return round(number, 2) / 1000

def string_to_float(input):
    if (input == 'None'):
        print('WARNING: Unexpected None value for column, defaulting to 0')
        return 0
    return float(input)

def calc_percent_increase(current, previous):
    if current <= 0 or previous <= 0:
        return 0
    increase = (current - previous) / previous
    return round(increase * 100, 2)
