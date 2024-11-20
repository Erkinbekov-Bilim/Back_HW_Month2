def fast_exponentiation(base, exponent):
    result = 1
    counter = 0
    while exponent > 0:
        counter+=1
        print(f"Ход: {counter}")
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result


print(fast_exponentiation(5, 8))