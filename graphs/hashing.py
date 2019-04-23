TABLE_SIZE = 1000
HASH_TABLE = [None for i in range(TABLE_SIZE)]

def get_hash_value(value):
    return hashing_with_reminder_method(value)


def hashing_with_reminder_method(value):
    return divmod(value, TABLE_SIZE)[-1]


def hashing_with_folding_method(value):
    fold_length = 2
    folds = []
    _value_str = str(value)
    _fold_points = list(range(0, len(_value_str), fold_length))
    print(_fold_points)
    for i, j in zip(_fold_points[:-1], _fold_points[1:]):
        folds.append(int(_value_str[i:j]))
    if _value_str[j:]:
        folds.append(int(_value_str[j:]))
    print(folds)
    return divmod(sum(folds), TABLE_SIZE)[-1]


def hashing_with_reminder_method(value):
    return divmod(value, TABLE_SIZE)[-1]


def hashing_with_reminder_method(value):
    return divmod(value, TABLE_SIZE)[-1]


def load_factor(value):
    global HASH_TABLE
    HASH_TABLE[get_hash_value(value)] = value
    return 'ok'


def search_value(value):
    if HASH_TABLE[get_hash_value(value)]:
        return True
    else:
        return False


if __name__ == '__main__':
    # sample_data = list(range(0, 121))
    # print(get_hash_value(12))
    # print(get_hash_value(112))
    # print(get_hash_value(212))
    # # add values
    # print(load_factor(12))
    # print(load_factor(112))
    # print(load_factor(212))
    # # find values
    # print(search_value(12))
    # print(search_value(112))
    # print(search_value(212))
    # print(search_value(312))
    # print(search_value(412))
    print(hashing_with_folding_method(123123123))
