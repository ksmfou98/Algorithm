def solution():
    s = input()
    str_split = s.split()
    result = []
    for i in str_split:
        result.append(i[::-1])
        result.append(" ")

    print("".join(result))


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        solution()