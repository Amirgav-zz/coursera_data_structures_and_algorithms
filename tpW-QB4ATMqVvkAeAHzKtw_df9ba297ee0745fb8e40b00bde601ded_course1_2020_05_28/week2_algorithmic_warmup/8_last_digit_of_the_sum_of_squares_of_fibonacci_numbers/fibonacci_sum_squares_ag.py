# Uses python3
from sys import stdin

def calc_fib_fast(n):
    fib_dict = {0: 0, 1: 1}
    if (n <= 1):
        return fib_dict[n]
    for i in range(2,n+1):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]

    return fib_dict[n]

def fibonacci_sum_squares_fast(n):

    n = n % 60

    fib_dict = {0: 0, 1: 1}
    if n>0:
        for i in range(2,n+2):
            fib_dict[i] = (fib_dict[i - 1] + fib_dict[i - 2])

    sum = (fib_dict[n+1] % 10) * (fib_dict[n] % 10)

    return sum % 10

if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_fast(n))
