def is_power_of_four(number: int) -> bool:
    while number > 1:
        if number % 4 != 0:
            return False
        number //= 4
    return True

print(is_power_of_four(int(input())))



def is_power_of_four(number: int) -> bool:
    import math
    if number <= 0:
        return False
    power = math.log(number, 4)
    return power.is_integer()

print(is_power_of_four(int(input())))