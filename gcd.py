# Uses python3
import sys

def gcd_opt(a, b):
    if b == 0:
        return a;
    remainder = a % b
    return gcd_opt(b, remainder)

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
#    print(gcd_naive(a, b))
    print(gcd_opt(a, b))
