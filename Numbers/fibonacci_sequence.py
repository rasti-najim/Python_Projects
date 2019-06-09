#  Enter a number and have the program generate
# the Fibonacci sequence to that number or to the Nth number.

n = int(input())
fib_seq = [0, 1]
n = int(input())


def fib_seq_generator(n):
    for i in range(1, n-1):
        rule = fib_seq[i] + fib_seq[i-1]
        fib_seq.append(rule)
    return fib_seq


fibonacci_sequence = fib_seq_generator(n)
print(fibonacci_sequence)
