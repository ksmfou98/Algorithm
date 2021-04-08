def solution(arr):
    a = []
    a.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            continue
        else:
            a.append(arr[i])
    return a