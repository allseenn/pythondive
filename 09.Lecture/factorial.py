import time
from typing import Callable

def main(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        return end - start
    return wrapper

def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

start = time.time()
factorial(1_000_000)
end = time.time()
print(end-start)

control = main(factorial)
print(control(1_000_000))