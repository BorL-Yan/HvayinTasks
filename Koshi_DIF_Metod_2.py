import math
from tabulate import tabulate


def f(x, y):
    return 0.185 * (x**2 + math.cos(0.7 * x)) + 1.843 * y
    #return 0.188 * (x**2 + math.sin(1.5 * x)) + 0.885 * y


x0 = 0.2  # initial point
y0 = 0.25  # initial condition
xn = 1.2  # end point
h = 0.1   # step
n = int((xn - x0) / h)  # step count

x_values = [x0]
y_values = [y0]
y_prime_values = [f(x0, y0)]
y_shirt_values = [] # y~_i+1
y_shirt_prime_values = []  # y~'_i+1


for i in range(n):
    x_i = x_values[i]
    y_i = y_values[i]
    y_prime_i = y_prime_values[i]

    # y~_{i+1}
    y_shirt_next = y_i + h * y_prime_i
    y_shirt_next = round(y_shirt_next, 4)
    y_shirt_values.append(y_shirt_next)

    # x_{i+1}
    x_next = x_i + h
    x_values.append(x_next)
    # y~'_{i+1}
    y_shirt_prime_next = f(x_next, y_shirt_next)
    y_shirt_prime_next = round(y_shirt_prime_next, 4)
    y_shirt_prime_values.append(y_shirt_prime_next)

    # y_{i+1}
    y_next = y_i + h/2 * (y_prime_i + y_shirt_prime_next)
    y_next = round(y_next, 4)
    y_values.append(y_next)

    # y'
    y_prime = f(x_next, y_next)
    y_prime = round(y_prime, 4)
    y_prime_values.append(y_prime)


table = []
for i in range(n + 1):
    row = [x_values[i], y_values[i], y_prime_values[i]]
    if i < n:
        row.extend([ y_shirt_values[i], y_shirt_prime_values[i]])
    else:
        row.extend(["-", "-"])
    table.append(row)

headers = ["x_i", "y_i", "y'_i", "y~_{i+1}", "y~'_{i+1}"]
print(tabulate(table, headers=headers, tablefmt="grid", floatfmt=".4f"))