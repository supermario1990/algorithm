"""
使用dict来缓存中间结果
"""
from typing import Dict

def fab(n: int) -> int:
    memo: Dict[int: int] = {0: 0, 1: 1}
    if n not in memo: 
        memo[n] = fab(n - 2) + fab(n - 1)
    return memo[n]