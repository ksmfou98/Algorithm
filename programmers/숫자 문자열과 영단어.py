def solution(s):
    number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    result = []
    s = list(s)
    i = 0
    while len(s) > 0:
        
        if s[0].isdigit():
            result.append(s[0])
            del s[0]
            
        if "".join(s[0:i]) in number:
            result.append(str(number.index("".join(s[0:i]))))
            del s[0:i]
            i = 0
        else:
            i += 1
    return int("".join(result))