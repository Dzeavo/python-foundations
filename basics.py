def analyze_numbers(numbers):
    positive_sum = 0
    negative_count = 0

    for n in numbers:
        if n > 0:
            positive_sum += n
        elif n < 0:
            negative_count += 1

    return positive_sum, negative_count


data = [10, -5, 3, -2, 0, 7]
result = analyze_numbers(data)
print(result)

