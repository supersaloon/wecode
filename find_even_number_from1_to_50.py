def even_number(start_number, end_number):
    even_numbers = []
    for i in range(start_number, end_number+1):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers


print(even_number(1, 50))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
