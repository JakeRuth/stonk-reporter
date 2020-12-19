def string_to_float(string_float):
    if (string_float == 'None'):
        print('WARNING: Unexpected None value for column, defaulting to 0')
        return 'ERROR'

    return round(float(string_float), 2)

 # TODO: Delete this and jsut use xlutils.get_column_letter you dumby
 # TODO: Rename this file to math utils or something
def convert_number_to_cell_value(number):
    stupid_cell_map = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H',
        9: 'I',
        10: 'J',
        11: 'K',
        12: 'L',
        13: 'M',
        14: 'N',
        15: 'O',
        16: 'P',
        17: 'Q',
        18: 'R',
        19: 'S',
        20: 'T',
        21: 'U',
        22: 'V',
        23: 'W',
        24: 'X',
        25: 'Y',
        26: 'Z',
    }
    return stupid_cell_map[number]
