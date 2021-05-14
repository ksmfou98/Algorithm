def solution(priorities, location):
    count = 0
    docs = priorities[:]
    docs[location] = "result"
    while 1:
        if priorities[0] == max(priorities) and docs[0] == "result":
            count += 1
            return count
        elif priorities[0] != max(priorities):
            priorities.append(priorities[0])
            del priorities[0]
            docs.append(docs[0])
            del docs[0]
        elif priorities[0] == max(priorities):
            count += 1
            del priorities[0]
            del docs[0]
        

priorities = [2,1,3,2]
location = 2
print(solution(priorities, location))