# ENSF 338 Assignment 2
# Sufyan Ayaz (30142184) amd Taha Khan (30145085)

def fib_remake(n, storage={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in storage:
            return storage[n]
        else:
            storage[n] = fib_remake(n-1) + fib_remake(n-2)
            return storage[n]
