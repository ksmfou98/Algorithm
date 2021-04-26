def solution(s, n):
    result = []

    for i in s:
        x = ord(i)
        if i == " ":
            result.append(" ")
            continue
        for j in range(n):
            x += 1
            if x == 123 or x == 91:
                x -= 26
        result.append(chr(x))

    result = "".join(result)
    return result