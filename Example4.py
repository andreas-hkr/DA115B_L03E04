from functools import cache


def fib(n, cache={}):
    if n <= 1:
        return n

    if n not in cache:
        cache[n] = fib(n - 1, cache) + fib(n - 2, cache)

    return cache[n]


@cache
# @lru_cache(maxsize=None)      # alt. does exactly the same
def fib2(n):
    if n <= 1:
        return n

    return fib2(n - 1) + fib2(n - 2)


def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def memo(func):         # Illustrates usagen of higher order functions
    cache = {}

    def memo_func(n):   # Closure, have access to cache even after memo finishes
        if n not in cache:
            cache[n] = func(n)
        return cache[n]

    return memo_func


fibonacci = memo(fibonacci)


def main():
    for i in range(100):
        print(f'{i:3d} : {fibonacci(i)}')
        print(f'{i:3d} : {fib(i)}')         # Only for showing an alternative implementation
        print(f'{i:3d} : {fib2(i)}')        # Only for showing an alternative using Pythons library


if __name__ == '__main__':
    main()
