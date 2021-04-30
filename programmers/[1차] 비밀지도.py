def solution(n, arr1, arr2):
    bin_arr1 = []
    bin_arr2 = []
    result = []


    for i in arr1:
        if len(bin(i)[2:]) < n:
            x = "0" * (n - len(bin(i)[2:]))
            x = x + bin(i)[2:]
            bin_arr1.append([x])
        else:
            x = bin(i)
            bin_arr1.append([x[2:]])
            
    for i in arr2:
        if len(bin(i)[2:]) < n:
            x = "0" * (n - len(bin(i)[2:]))
            x = x + bin(i)[2:]
            bin_arr2.append([x])
        else:
            x = bin(i)
            bin_arr2.append([x[2:]])
            
    for i in range(n):
        li = []
        for j in range(n):
            if int(bin_arr1[i][0][j]) + int(bin_arr2[i][0][j]) == 2 or int(bin_arr1[i][0][j]) + int(bin_arr2[i][0][j]) == 1:
                li.append("#")
            else:
                li.append(" ")
        li = "".join(li)
        result.append(li)
    
    return result

