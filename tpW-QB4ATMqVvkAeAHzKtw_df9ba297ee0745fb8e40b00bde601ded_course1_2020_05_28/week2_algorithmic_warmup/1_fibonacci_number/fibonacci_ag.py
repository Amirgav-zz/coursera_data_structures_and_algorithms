# Uses python3
def calc_fib_fast(n):
    fib_dict = {0: 0, 1: 1}
    if (n <= 1):
        return fib_dict[n]
    for i in range(2,n+1):
        fib_dict[i] = fib_dict[i - 1] + fib_dict[i - 2]

    return fib_dict[n]

n = int(input())
print(calc_fib_fast(n))
