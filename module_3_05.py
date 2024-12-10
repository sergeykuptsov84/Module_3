def get_multiplied_digits(number):
    a = str(number)
    str_number = a.replace('0', '')    # all elements '0' removed to avoid multiplication by ZERO
    first = int(str_number[0])

    if len(str_number) <= 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)       # 4*2*3=24
print(result)
result2 = get_multiplied_digits(402030)     # 4*2*3=24
print(result2)