import time
import cProfile


def fib(n):
    if n < 2: return 1
    return fib(n - 1) + fib(n - 2)


start = time.time()
fib(39)
# cProfile.run('fib(39)')
end = time.time()
print(f'Time taken: {end - start}')