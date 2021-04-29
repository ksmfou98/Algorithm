def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        li = []
        for j in range(len(arr1[0])):
            x = arr1[i][j] + arr2[i][j]
            li.append(x)
        result.append(li)
    
    return result
        