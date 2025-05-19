import math
from tabulate import tabulate


def f(x, y):
    return 0.185 * (x**2 + math.cos(0.7 * x)) + 1.843 * y
    #return 0.188 * (x**2 + math.sin(1.5 * x)) + 0.885 * y


x0 = 0.2  # initial poit
y0 = 0.25  # initial condition
xn = 1.2  # end point
h = 0.1  # step
n = int((xn - x0) / h)  # step count


x_values = [x0]
y_values = [y0]
y_prime_values = [f(x0, y0)]
y_half_values = [] # y_{i+1/2}
y_prime_half_values = [] # y'_{i+1/2}

x_half_values = []

for i in range(n):
    x_i = x_values[i]
    y_i = y_values[i]
    y_prime_i = y_prime_values[i]
    
    #  y_{i+1/2}
    y_half = y_i + (h / 2) * y_prime_i
    y_half = round(y_half, 4) 
    y_half_values.append(y_half)
    
    # x_{i+1/2} и y'_{i+1/2}
    x_half = x_i + h / 2
    y_prime_half = f(x_half, y_half)
    y_prime_half = round(y_prime_half, 4) 
    y_prime_half_values.append(y_prime_half)
    
    x_half = round(x_half, 4)
    x_half_values.append(x_half)
    # y_{i+1}
    y_next = y_i + h * y_prime_half
    y_next = round(y_next, 4)  
    x_next = x_i + h
    x_next = round(x_next, 4)  

    y_prime = f(x_next, y_next)
    y_prime = round(y_prime, 4)

    x_values.append(x_next)
    y_values.append(y_next)
    y_prime_values.append(y_prime)


table = []
for i in range(n + 1):
    row = [x_values[i], y_values[i], y_prime_values[i]]
    if i < n:
        row.extend([ x_half_values[i], y_half_values[i], y_prime_half_values[i]])
    else:
        row.extend(["-", "-", "-"])
    table.append(row)


headers = ["x_i", "y_i", "y'_i", "x_i+h/2", "y_{i+1/2}", "y'_{i+1/2}"]
print(tabulate(table, headers=headers, tablefmt="grid", floatfmt=".4f"))