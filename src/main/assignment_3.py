# Euler Method
def euler(y0, t0, h, iters):
    y = [y0] # List storing y starting at y0
    t = [t0] # List storing t starting at t0
 
    for i in range(iters):
        y_next = y[i] + h * func(t[i], y[i])
        t_next = t[i] + h
        
        y.append(y_next) # Add the values to the list
        t.append(t_next)
    
    print(y[-1], "\n") # Print the final/last value

def func(t, y):
    return t - y**2

#Runge-Kutta Method
def runge_kutta(y0, t0, h, iters):
    y = [y0]
    t = [t0]
    w = []
    
    for i in range(iters):
        k1 = func(t[i], y[i])
        k2 = func(t[i] + (h / 2), y[i] + (h / 2) * k1)
        k3 = func(t[i] + (h / 2), y[i] + (h / 2) * k2)
        k4 = func(t[i] + h, y[i] + (h * k3))

        y_next = y[i] + (h / 6) * (k1 + (2 * k2) + (2 * k3) + k4)
        t_next = t[i] + h
        
        y.append(y_next)
        t.append(t_next)
        
    print(y[-1], "\n") # Print the final/last value
    