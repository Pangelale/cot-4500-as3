# Import functions from main file
from main.assignment_3 import euler
from main.assignment_3 import runge_kutta

t0 = 0
y0 = 1
h = 0.2
iters = 10

# Test Euler Method
euler(y0, t0, h, iters)

# Test Euler Method
runge_kutta(y0, t0, h, iters)