import numpy as np

def basic_stats_np(numbers):
    data = np.array(numbers)

    mean = data.mean()
    minimum = data.min()
    maximum = data.max()

    return mean, minimum, maximum


data = [10, -5, 3, 7, 0]
print(basic_stats_np(data))

