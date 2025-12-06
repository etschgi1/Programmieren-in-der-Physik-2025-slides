from uncertainties.umath import sin, cos
from uncertainties import ufloat

angle = ufloat(0.5, 0.05)  # 0.5 +/- 0.05
sine_value = sin(angle)
cosine_value = cos(angle)
print(sine_value)  # 0.48 +/- 0.04
print(cosine_value)  # 0.878 +/- 0.024