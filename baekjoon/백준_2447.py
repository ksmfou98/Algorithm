import sys

input = sys.stdin.readline


def solution(N: int) -> None:
    Num = N
    makeStar(Num, N)
    while Num >= 3:
        makeStar(Num // 3, N, N // (Num // 3))
        Num = Num // 3

    for i in star:
        print(i)


def makeStar(n: int, N: int, count=1) -> None:
    for k in range(N // n):
        for i in range((n // 3) + (n * k), (n // 3) * 2 + (n * k)):  # 세로줄 기준
            changeStar = list(star[i])  # 리스트로 바꿔서
            for j in range(count):  # 조건에 만족하는 부분의 *을 공백으로 바꿔줌
                changeStar[(n // 3) + (j * n) : (n // 3) * 2 + (j * n)] = " " * (n // 3)
            star[i] = "".join(changeStar)  # 바꿔준걸 실제 리스트에 적용


if __name__ == "__main__":
    N = int(input())
    star = ["*" * N] * N
    solution(N)