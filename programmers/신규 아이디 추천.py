import re


def solution(new_id):

    new_id = new_id.lower()

    result = []
    for i in new_id:
        if i.isalnum() or i in "-_.":
            result.append(i)

    new_id = "".join(result)

    for i in range(len(new_id) // 2):
        new_id = new_id.replace("..", ".")

    if new_id[0] == ".":
        new_id = list(new_id)
        new_id.remove(".")
        new_id = "".join(new_id)
    if len(new_id) > 0:
        if new_id[len(new_id) - 1] == ".":
            new_id = list(new_id)
            del new_id[len(new_id) - 1]
            new_id = "".join(new_id)

    if len(new_id) == 0:
        new_id = "a"

    if len(new_id) >= 16:
        new_id = list(new_id)
        del new_id[15:]
        new_id = "".join(new_id)

    if new_id[len(new_id) - 1] == ".":
        new_id = list(new_id)
        del new_id[len(new_id) - 1]
        new_id = "".join(new_id)

    while len(new_id) <= 2:
        new_id = list(new_id)
        new_id.append(new_id[len(new_id) - 1])
        new_id = "".join(new_id)

    return new_id


