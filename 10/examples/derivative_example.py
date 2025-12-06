from scipy.misc import derivative

def f(x):
    return x**3 + x**2

deriv = derivative(f, 1.0, dx=1e-6)
print("Derivative:", deriv)
