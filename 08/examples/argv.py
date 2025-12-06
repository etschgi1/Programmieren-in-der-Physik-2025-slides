import sys
def calcprimes(n):
    return [i for i in range(1, n+1) if all(i % j for j in range(2, i))]

if __name__ == '__main__':
    print(calcprimes(int(sys.argv[1])))