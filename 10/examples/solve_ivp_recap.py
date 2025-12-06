import numpy as np
from scipy.integrate import solve_ivp

def dydt(t, y):
    return -0.5 * y

sol = solve_ivp(dydt, [0, 10], [2])
print("Solution of the ODE:", sol.y)
