def convert_to_binary(val):
    if type(val) != int:
        raise ValueError("Please enter a valid integer")

    if val == 0:
        return "0b0"

    binary_string = ""
    valid_places = {}
    invalid_places = {}

    base2calc = -1

    starting_exponent = 0

    while base2calc <= val:
        base2calc = 2 ** starting_exponent
        starting_exponent += 1

    highest_power = starting_exponent - 1

    power_list = sorted(map(lambda x: 2**x, list(range(highest_power))),
                        reverse=True)

    for i in power_list:
        if val - i >= 0:
            val = val - i
            valid_places[i] = "1"
        else:
            continue

    for i in power_list:
        if i not in valid_places:
            invalid_places[i] = "0"

    valid_places = list(tuple(valid_places.items()))
    invalid_places = list(tuple(invalid_places.items()))

    valid_places.extend(invalid_places)

    final = sorted(valid_places, key=lambda x: x[0], reverse=True)

    for i in final:
        binary_string += i[1]

    return "0b" + binary_string


# unit tests

assert convert_to_binary(79) == bin(79)
assert convert_to_binary(0) == bin(0)
assert convert_to_binary(100) == bin(100)
assert convert_to_binary(999) == bin(999)
