def fib_iterative(n):
    if n < 2: 
        return n 
    prev, curr = 0, 1
    for i in range(n-1):
        prev, curr = curr, prev + curr
    return curr

def fib_recursive(n):
    if n < 2: 
        return n 
    return fib_recursive(n-1) + fib_recursive(n-2)


if __name__ == "__main__":
    #run benchmark
    import timeit
    print("Time for fib_iterative(20) for 1000 runs:")
    print(str(timeit.timeit("fib_iterative(20)", setup="from __main__ import fib_iterative", number=1000))+ " s")
    print("Time for fib_recursive(20) for 1000 runs:")
    print(str(timeit.timeit("fib_recursive(20)", setup="from __main__ import fib_recursive", number=1000))+ " s")