def check(input_val):
    rslt = 0
    if input_val % 4 != 0:
        return rslt
    if input_val % 100 == 0:
        if input_val % 400 == 0:
            rslt = 1
            return rslt
        return rslt
    rslt = 1
    return rslt

a = int(input())
print(check(a))

