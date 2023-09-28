def disarium_number(number):
    str_number = [x for x in str(number)]
    result = [int(val) ** idx for idx, val in enumerate(str_number, 1)]
    return "Disarium !!" if number == sum(result) else "Not !!"


print(disarium_number(101))  # 5 ** 1 + 1 ** 2 + 8 **3  = 518