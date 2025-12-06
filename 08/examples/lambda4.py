import numpy as np
prime_test = lambda x,y: True if x % y else False
x = np.arange(1, 101)
primes = [i for i in x if all(prime_test(i,j) for j in range(2, i))]
print(primes[:5]) # [1, 2, 3, 5, 7]