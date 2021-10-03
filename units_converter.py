def kmh_to(from_unit, operation_number):
    convert_operations = [from_unit,
                          (from_unit*10/36),
                          (from_unit*0.621371),
                          (from_unit*0.621371/3600)]
    return round(convert_operations[operation_number-1], 3)


def ms_to(from_unit, operation_number):
    convert_operations = [(from_unit * 36/10),
                          from_unit,
                          (from_unit * 2.23694),
                          (from_unit * 0.000621371)]
    return round(convert_operations[operation_number-1], 3)


def mph_to(from_unit, operation_number):
    convert_operations = [(from_unit*1.60934),
                          (from_unit*0.44704),
                          from_unit,
                          (from_unit/3600)]
    return round(convert_operations[operation_number-1], 3)


def mps_to(from_unit, operation_number):
    convert_operations = [(from_unit*1.60934*3600),
                          (from_unit*0.44704*3600),
                          (from_unit*3600),
                          from_unit]
    return round(convert_operations[operation_number-1], 3)


list_of_function = [kmh_to, ms_to, mph_to, mps_to]


if __name__ == '__main__':
    print("There are:\n1)km/h\n2)m/s\n4)mph\n5)mps\nAnd that's all")
    while True:
        try:
            unit_from = int(input('Choose the NUMBER FROM ***: '))
            value = float(input('value: '))
            unit_to = int(input('Just choose the NUMBER TO ***: '))
            if (0 < unit_from < 5) and (0 < unit_to < 5):
                print(list_of_function[unit_from-1](value, unit_to))
            else:
                print("You can't count, can you? ")
                continue
            if input('Again? [y/any]') == 'y':
                continue
            else:
                break
        except ValueError:
            print('It is not a NUMBER!')
            continue
