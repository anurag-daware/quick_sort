# Uses python3
import sys

def gcd_opt(a, b):
    if b == 0:
        return a;
    remainder = a % b
    return gcd_opt(b, remainder)

def lcm(a, b):
    return((int(a / gcd_opt(a, b))) * b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

