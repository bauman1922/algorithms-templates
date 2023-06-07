from typing import List


def factorize(number: int) -> List[int]:
    lst = []
    chislo = 2
    while chislo * chislo <= number:
        if number % chislo == 0:
            lst.append(chislo)
            number = number // chislo
        else:
            chislo += 1
    if number > 1:
        lst.append(number)
    return lst


result = factorize(int(input()))
print(" ".join(map(str, result)))



from typing import List

# ДОЛГОЕ ВРЕМЯ ИСПОЛНЕНИЯ КОДА
def factorize(number: int) -> List[int]:
    lst = []
    chislo = 2
    while number > 1:
        if number % chislo == 0:
            lst.append(chislo)
            number = number / chislo
        else:
            chislo += 1
    return lst


result = factorize(int(input()))
print(" ".join(map(str, result)))