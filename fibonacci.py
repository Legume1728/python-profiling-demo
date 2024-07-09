import time
import cProfile


# to run this with cProfile
# python3 -m cProfile  -s cumtime fibonacci.py | head -n 20

def fib(n):
    if n < 2: return 1
    return fib(n - 1) + fib(n - 2)

start = time.time()
fib(39)
# cProfile.run('fib(39)')
end = time.time()
print(f'Time taken: {end - start}')
