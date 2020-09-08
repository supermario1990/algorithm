"""
使用dict来缓存中间结果
"""
from typing import Dict

def fib(n: int) -> int:
    memo: Dict[int: int] = {0: 0, 1: 1}
    if n not in memo: 
        memo[n] = fib(n - 2) + fib(n - 1)
    return memo[n]