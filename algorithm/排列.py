from typing import List


def pailie(stack:List[int],source:List,cur,target):
    if len(stack) == target:
        print(stack)
        return

    for i in range(cur,4):
        if not source[i] in stack:
            stack.append(source[i])
            pailie(stack,source,i,target)
            stack.pop()

source = [1,2,3,4]
stack = []
pailie(stack,source,0,3)