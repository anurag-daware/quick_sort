# Uses python3
import sys

def get_fibonacci_huge(n, m):
    if n <= 1:
        return 1

    previous = 0
    current  = 1
    pisano_sequence = [0, 1]
    bSequenceFound = False
    pisano_period = 2

    for x in range((m * m) + 1):
        previous, current = current, previous + current
        pisano_sequence.append(current % m)
        #print(current % m, end =" ")
        if (pisano_sequence[-1] == 1) and (pisano_sequence[-2] == 0):
            bSequenceFound = True
            pisano_sequence = pisano_sequence[:-2]
            pisano_period = len(pisano_sequence)
            break

    if(bSequenceFound):
        remainder = n % pisano_period
        return(pisano_sequence[remainder])
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(str(get_fibonacci_huge(n, m)))
