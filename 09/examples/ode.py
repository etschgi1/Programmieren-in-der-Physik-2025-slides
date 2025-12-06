import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
# Define the ODE as a function
def dydt(t, y):
    return -2 * y
# Initial condition
y0 = [1]
# Time points where we want the solution
t_span = (0, 5)
t_eval = np.linspace(0, 5, 100)
# Solve the ODE
solution = solve_ivp(dydt, t_span, y0, t_eval=t_eval)
t, y = solution.t, solution.y[0]
# Plot the solution ...
plt.plot(solution.t, solution.y[0])
plt.xlabel('Time t')
plt.ylabel('y(t)')
plt.title('Solution of the ODE dy/dt = -2y')
plt.grid()
plt.show()
