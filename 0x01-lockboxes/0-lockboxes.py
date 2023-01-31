#!/usr/bin/python3

def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened."""
    n = len(boxes)
    mylist = [0]
    for i in mylist:
        for j in boxes[i]:
            if j not in mylist:
                if j < n:mylist.append(j)
    if len(mylist) == n:
        return True
    return False