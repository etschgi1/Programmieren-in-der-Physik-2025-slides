def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        a = 1
        b = 1
        while n > 1:
            a, b = b, a + b
            n = n - 1
        return b
