import numpy as np
my_array = np.arange(1, 5, dtype=float)
el_wise = np.reciprocal(my_array) 
print(el_wise) # [1. 0.5 0.33333 0.25]
# vs
my_array[0] = 1 / my_array[0]
my_array[1] = 1 / my_array[1]
my_array[2] = 1 / my_array[2]
my_array[3] = 1 / my_array[3]
print(my_array) # [1. 0.5 0.33333 0.25]
