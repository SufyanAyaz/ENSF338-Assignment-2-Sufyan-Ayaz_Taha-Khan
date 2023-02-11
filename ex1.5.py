import timeit
import matplotlib.pyplot as plt


def func1(n):
    if n == 0 or n == 1:
        return n
    else:
        return func1(n-1) + func1(n-2)


def fib_remake(n, storage={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in storage:
            return storage[n]
        else:
            storage[n] = fib_remake(n-1) + fib_remake(n-2)
            return storage[n]


time_complexity_func1 = []
time_complexity_func2 = []

for i in range(0, 36):
    time_func1 = timeit.timeit(
        f"func1({i})", number=1, globals=globals())
    time_complexity_func1.append(time_func1)

    time_func2 = timeit.timeit(
        f"fib_remake({i})", number=1, globals=globals())
    time_complexity_func2.append(time_func2)

plt.plot(time_complexity_func1, label='func1')
plt.plot(time_complexity_func2, label='fib_remake')
plt.xlabel('Input size')
plt.ylabel('Time taken (in seconds)')
plt.legend()
plt.show()
