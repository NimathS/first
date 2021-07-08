def sum_numbers(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

# print(sum_numbers((10, 10, 11)))

def multiply_numbers(numbers):
    result = 1
    for y in numbers:
        result *= y
    return result

# print(multiply_numbers((10, 10)))

def raise_pow_num(base, pow_num):
    result = 1
    for index in range(pow_num):
        result = base * result
    return result

# print(raise_pow_num(3, 2))

def simple(number):
    return number * 2

print(simple(10))
