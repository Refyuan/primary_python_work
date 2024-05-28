from typing import List


def isAlone(num):
    a = str(num)
    b = []
    flag = True
    for i in a:
        if b.__contains__(i):
            flag = False
            break
        b.append(i)
    return flag


def isAlone2(list: List):
    a = ""
    for i in list:
        a = a + str(i)
    return isAlone(a)


def isLen10(list: List):
    flag = 0
    a = ""
    for i in list:
        a = a + str(i)
    if len(a) == 10:
        flag = 1
    elif len(a) > 10:
        flag = 2
    else:
        flag = 0
    return flag


def dfs(list: List, list2: List, curIndex):
    global count
    if isLen10(list2) == 1:
        if isAlone2(list2):
            count += 1
            print(list2)
        else:
            return
    elif isLen10(list2) == 2:
        return

    for index in range(curIndex, len(list)):
        list2.append(list[index])
        dfs(list, list2, index + 1)
        list2.remove(list[index])


if __name__ == '__main__':
    count = 0
    list = []
    for i in range(100001):
        a = i * i
        if a <= 9876543210 and isAlone(a):
            list.append(a)
    print(list)
    list2 = []
    dfs(list, list2, 0)
    print(count)
