"""
使用lru_cache缓存函数结果
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    print(n)
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    print(fib(10))

