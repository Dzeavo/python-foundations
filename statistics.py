def basic_stats(numbers):
    total = 0
    count = 0

    minimum = numbers[0]
    maximum = numbers[0]

    for n in numbers:
        total += n
        count += 1

        if n < minimum:
            minimum = n

        if n > maximum:
            maximum = n

    mean = total / count

    return mean, minimum, maximum


data = [10, -5, 3, 7, 0]
print(basic_stats(data))
