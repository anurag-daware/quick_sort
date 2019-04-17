# Uses python3
import sys

def get_fibonacci_last_digit_linear(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    i = 2
    while (i <= n):
        prev, curr = curr, (prev + curr)%10
        i += 1
    return curr

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_linear(n))
