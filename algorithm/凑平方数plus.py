from typing import List

list = []
for i in range(100001):
    a = i * i
    if a <= 9876543210:
        list.append(a)
list2 = []


def check_alone(i):
    list1 = []
    isAlone = True
    for j in str(i):
        if list1.__contains__(j):
            isAlone = False
            break
        else:
            list1.append(j)
    return isAlone


def check_alone_list(list):
    m_str = ""
    for i in list:
        m_str += str(i)
    return check_alone(m_str)


for i in list:
    isAlone = check_alone(i)
    if isAlone == True:
        list2.append(i)


def count_list(list3):
    str1 = ""
    for i in list3:
        s = str(i)
        str1 = str1 + s
    return len(str1)


def dfs(list2, list3: List, index):
    global count
    if count_list(list3) >= 10:
        if count_list(list3) == 10 and check_alone_list(list3) == True:
            count += 1
            print(list3)
        return
    for cur_index in range(index, len(list2)):
        i = list2[cur_index]
        list3.append(i)
        dfs(list2, list3, cur_index + 1)
        list3.pop()


stack = []
count = 0
dfs(list2, stack, 0)
print(count)