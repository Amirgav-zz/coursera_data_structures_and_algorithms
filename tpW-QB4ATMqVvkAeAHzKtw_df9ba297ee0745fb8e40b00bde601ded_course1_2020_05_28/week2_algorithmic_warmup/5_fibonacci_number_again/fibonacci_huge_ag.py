# Uses python3
import sys

def get_pisano_period(m):
    previous = 0
    current = 1
    for i in range(m**2):
        previous, current = current, (previous + current) % m
        if (previous == 0 and current ==1):
            return i+1

def get_fibonacci_huge_fast(n, m):

    pisano_period = get_pisano_period(m)

    n = n % pisano_period

    if n == 0:
        return 0
    elif n == 1:
        return 1

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))



