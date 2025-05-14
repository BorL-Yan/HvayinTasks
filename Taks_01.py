import math

# Define the function y' = f(x, y) = 0.188 * (x^2 + sin(1.5x)) + 0.885y
def f(x, y):
    return 0.185 * (x**2 + math.cos(0.7 * x)) + 0.843 * y

# Parameters
x0 = 0.2  # Initial x
y0 = 0.25  # Initial y
h = 0.1   # Step size
x_end = 1.2  # End of interval
n = int((x_end - x0) / h) + 1  # Number of points

# Lists to store results
x_values = [x0]
y_values = [y0]

#Book Version
# y_i+1 = y_i + h/2 * (y'_i + y~_i+1)

### y~_i+1 = y'(x_i+1, y~_i+1) ????
### y~_i+1 = y_i + h * y_i

#GPT Version
# y' = f(x,y)
#y_i+1 = y_i + h/2 * (f(x_i,y_i) + f(x_i+1,y~_i+1))

# y~_i+1 = y_i + h * f(x_i, y_i)

# Improved Euler method
for i in range(n - 1):
    x_n = x_values[-1]
    y_n = y_values[-1]
    
    # Predictor step
    k1 = f(x_n, y_n)
    y_tilde = y_n + h * k1
    
    # Corrector step
    x_next = x_n + h
    k2 = f(x_next, y_tilde)
    y_next = y_n + (h / 2) * (k1 + k2)
    
    # Round to 4 decimal places
    y_next = round(y_next, 4)
    x_next = round(x_next, 4)
    
    x_values.append(x_next)
    y_values.append(y_next)

# Print results
print("|  x_n  |   y_n  |")
print("|-------|--------|")
for x, y in zip(x_values, y_values):
    print(f"|  {x:.1f}  | {y:.4f} |")