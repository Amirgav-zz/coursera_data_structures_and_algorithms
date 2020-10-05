# Uses python3
import sys

def gcd_fast(a, b):
    b, a = min(a,b), max(a,b)
    if b ==0:
        return a
    else:
        a_prime = a % b
        return gcd_fast(a_prime, b)

def lcm_fast(a, b):

    return int(abs(a*b) / gcd_fast(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

