import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

# Define the function to be integrated
def f(x):
    return x**2

# Integration boundaries
a = 0
b = 2

# Monte Carlo method parameters
num_points = 10000
x_random = np.random.uniform(a, b, num_points)
y_random = f(x_random)

# Monte Carlo integration result
monte_carlo_integral = (b - a) * np.mean(y_random)

# Analytical integration using quad
quad_result, quad_error = spi.quad(f, a, b)

# Plotting the function and the integration area
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()

# Draw the function
ax.plot(x, y, 'r', linewidth=2)

# Fill the area under the curve
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Set up the graph
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Add integration limits and graph title
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Graph of integration of f(x) = x^2 from ' + str(a) + ' to ' + str(b))
plt.grid()
plt.show()

# Output the results
print("Monte Carlo Integral: ", monte_carlo_integral)
print("Quad Integral: ", quad_result)
print("Quad Error Estimate: ", quad_error)
