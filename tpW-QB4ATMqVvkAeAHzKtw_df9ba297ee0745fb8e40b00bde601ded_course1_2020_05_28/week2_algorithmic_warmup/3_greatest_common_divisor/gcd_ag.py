# Uses python3
import sys

def gcd_fast(a, b):
    b, a = min(a,b), max(a,b)
    if b ==0:
        return a
    else:
        a_prime = a % b
        return gcd_fast(a_prime, b)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_fast(a, b))
