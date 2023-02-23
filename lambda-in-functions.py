# PEP 8: E731 do not assign a lambda expression, use a def
def egg_dozens(n):
    return lambda x: x + n


new_dozens = egg_dozens(12)  # pass in arg for n: n = 12
print(new_dozens(2))         # pass in arg for lambda function: x = 2


def myfunc(x):
    return lambda n: n + x


new_century = myfunc(100)
print(new_century(2000))


def sum_times(x):
    return lambda a, b : (a + b) * x    # (10 + 20) * 2


sum_times_2 = sum_times(2)
print(sum_times_2(10, 20))
