"""
使用lru_cache缓存函数结果
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def fab(n: int) -> int:
    print(n)
    if n < 2:
        return n
    return fab(n - 1) + fab(n - 2)

if __name__ == "__main__":
    print(fab(10))

