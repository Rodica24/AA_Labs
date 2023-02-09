import time
import math
from prettytable import PrettyTable
import matplotlib.pyplot as plt

def fib_recursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

n_values = list(range(1, 31))
table = PrettyTable(["n", "Result", "Time (seconds)"])
times = []
for n in n_values:
    start_time = time.time()
    result = fib_recursive(n)
    end_time = time.time()
    time_taken = end_time - start_time
    table.add_row([n, result, time_taken])
    times.append(time_taken)

print(table)

plt.plot(n_values, times)
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time taken (seconds)")
plt.title("Execution time of recursive function")
plt.show()

def fib_iterative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        prev1 = 0
        prev2 = 1
        for i in range(2, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        return prev2
n = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
time1 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.001, 0.001, 0.002, 0.003]
plt.plot(n, time1)
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time taken (seconds)")
plt.title("Execution time of iterative function")
plt.show()

def fib_dp(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]


time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.001, 0.002, 0.003, 0.004, 0.007]
plt.plot(n, time)
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time taken (seconds)")
plt.title("Execution time of dynamic programming method")
plt.show()

def matrix_mult(A, B):
    C = [[0, 0], [0, 0]]
    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    return C


def fib_matrix(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        A = [[1, 1], [1, 0]]
        B = [[1, 1], [1, 0]]
        for i in range(2, n):
            B = matrix_mult(A, B)
        return B[0][0]


time = [0.0, 0.0, 0.0, 0.0, 0.001, 0.001, 0.002, 0.002, 0.003, 0.005, 0.013, 0.012, 0.017, 0.031, 0.042, 0.056]
plt.plot(n, time)
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time taken (seconds)")
plt.title("Execution time of matrix multiplication method")
plt.show()

def fibonacci_closed_form(n):
    if n<=1:
        return n
    else:
        golden_ratio = (1 + math.sqrt(5)) / 2
        return int(round((golden_ratio**n - (1 - golden_ratio)**n) / math.sqrt(5)))

time = [0.008, 0.012, 0.015, 0.018, 0.023, 0.025, 0.028, 0.03, 0.034, 0.036, 0.04, 0.048, 0.056, 0.061, 0.065, 0.085]
plt.plot(n, time)
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time taken (seconds)")
plt.title("Execution time of closed form method")
plt.show()

def fib_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))

time = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002, 0.0002, 0.0005]
plt.plot(n, time)
plt.xlabel("n-th Fibonacci Term")
plt.ylabel("Time taken (seconds)")
plt.title("Execution time of Binet Formula method")
plt.show()

table = PrettyTable()
table.field_names = ['', 501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849]
table.add_row(['Iterative', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.0, 0.001, 0.001, 0.002, 0.003])
table.add_row(['Dynamic programming', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.001, 0.002, 0.003, 0.004, 0.007])
table.add_row(['Matrix multiplication',0.0, 0.0, 0.0, 0.0, 0.001, 0.001, 0.002, 0.002, 0.003, 0.005, 0.013, 0.012, 0.017, 0.031, 0.042, 0.056])
table.add_row(['Closed form',0.008, 0.012, 0.015, 0.018, 0.023, 0.025, 0.028, 0.03, 0.034, 0.036, 0.04, 0.048, 0.056, 0.061, 0.065, 0.085])
table.add_row(['Binet method', 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.002, 0.0002, 0.0005])
print(table)