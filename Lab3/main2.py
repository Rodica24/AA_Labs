import time
import math
import matplotlib.pyplot as plt

def sieve_of_eratosthenes_1(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2
    while i <= n:
        if c[i]:
            j = 2 * i
            while j <= n:
                c[j] = False
                j = j + i

        i = i + 1

    return c


def sieve_of_eratosthenes_2(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2

    while i <= n:
        j = 2 * i
        while j <= n:
            c[j] = False
            j = j + i
        i = i + 1
    return c


def sieve_of_eratosthenes_3(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2

    while i <= n:
        if c[i]:
            j = i + 1
            while j <= n:
                if j % i == 0:
                    c[j] = False
                j = j + 1
        i = i + 1

    return c


def sieve_of_eratosthenes_4(n):
    c = [True] * (n + 1)
    c[1] = False
    i = 2

    while i <= n:
        j = 2
        is_prime = True
        while j < i:
            if i % j == 0:
                is_prime = False
                break
            j = j + 1
        if not is_prime:
            c[i] = False
        i = i + 1

    return c


def sieve_of_eratosthenes_5(n):
    c = [True] * (n + 1)
    c[0] = c[1] = False
    i = 2
    while (i <= n):
        j = 2
        while (j <= math.sqrt(i)):
            if (i % j == 0):
                c[i] = False
            j += 1
        i += 1
    return c

def exec_time(function, n):
    start_time = time.time()
    function(n)
    end_time = time.time()
    return end_time - start_time


n = 4000

t1 = exec_time(sieve_of_eratosthenes_1, n)
t2 = exec_time(sieve_of_eratosthenes_2, n)
t3 = exec_time(sieve_of_eratosthenes_3, n)
t4 = exec_time(sieve_of_eratosthenes_4, n)
t5 = exec_time(sieve_of_eratosthenes_5, n)

print("Algorithm 1 - " , t1, "s")
print("Algorithm 2 - " , t2, "s")
print("Algorithm 3 - " , t3, "s")
print("Algorithm 4 - " , t4, "s")
print("Algorithm 5 - " , t5, "s")


Algorithms = [
    {
        "name": "Algorithm 1",
        "alg": lambda n: sieve_of_eratosthenes_1(n)
    },
    {
        "name": "Algorithm 2",
        "alg": lambda n: sieve_of_eratosthenes_2(n)
    },
    {
        "name": "Algorithm 3",
        "alg": lambda n: sieve_of_eratosthenes_3(n)
    },
    {
        "name": "Algorithm 4",
        "alg": lambda n: sieve_of_eratosthenes_4(n)
    },
    {
        "name": "Algorithm 5",
        "alg": lambda n: sieve_of_eratosthenes_5(n)
    }
]

times = []

for alg in Algorithms:
    exec_times = []
    for i in range(1, 5):
        exec_t = exec_time(alg["alg"], i * 1000)
        exec_times.append(exec_t)
    times.append(exec_times)

x_axis = [i * 1000 for i in range(1, 5)]

plt.title('Execution Time Comparison')
plt.plot(x_axis, times[0], label=Algorithms[0]["name"])
plt.plot(x_axis, times[1], label=Algorithms[1]["name"])
plt.plot(x_axis, times[2], label=Algorithms[2]["name"])
plt.plot(x_axis, times[3], label=Algorithms[3]["name"])
plt.plot(x_axis, times[4], label=Algorithms[4]["name"])

plt.xlabel('Input = n')
plt.ylabel('Time ')

plt.grid()
plt.legend()
plt.show()