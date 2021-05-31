import sys
from typing import List

input = sys.stdin.readline


def solution(N: int, A: List[int], B: List[int]) -> int:
    S = 0
    for i in range(N):
        S += min(A) * max(B)
        A.remove(min(A))
        B.remove(max(B))
    return S


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solution(N, A, B))