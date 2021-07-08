def sum_numbers(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

print(sum_numbers((10, 10, 11)))

def multiply_numbers(numbers):
    result = 1
    for y in numbers:
        result *= y
    return result

print(multiply_numbers((10, 10)))
