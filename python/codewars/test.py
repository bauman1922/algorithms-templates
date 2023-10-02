def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    else:
        arr = []
    while lng > 0 and wdth > 0:
        if lng >= wdth:
            arr.append(wdth)
            lng -= wdth
        elif lng < wdth:
            arr.append(lng)
            wdth -= lng
    return arr



print(sq_in_rect(20, 14))   # [14, 6, 6, 2, 2, 2]