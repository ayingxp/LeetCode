# 用递归计算阶乘
from functools import lru_cache
from functools import wraps

def memorize(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            res = function(*args)
            memo[args] = res
            return res
    return wrapper


def fact(n):
    if n in [0, 1]:
        return 1
    else:
        return n * fact(n-1)

# @lru_cache()
def fib(n):
    if n in [0, 1]:
        return n
    else:
        return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    n = 150
    # res = fact(n)
    import time
    start = time.time()
    res = fib(n)
    print(res)
    print("Total time is: ", time.time() - start)