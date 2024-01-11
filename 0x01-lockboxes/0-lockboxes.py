#!/usr/bin/python3
""" Lockboxes """


def canUnlockAll(boxes):
    """ Determines whether all the locked boxes can be opened,
    given a list of locked boxes represented as a list of lists.
    Each box is numbered sequentially from 0 to n - 1,
    and a key with the same number as a box can open that box.
    The function starts with the first box (boxes[0]) unlocked and
    iteratively explores and unlocks other boxes using the keys found
    in already unlocked boxes.
    """

    openedBoxIndices = [0]
    for idx in openedBoxIndices:
        print(idx)
        for ele in boxes[idx]:
            if ele not in openedBoxIndices and ele < len(boxes):
                openedBoxIndices.append(ele)
    if len(openedBoxIndices) == len(boxes):
        return True
    else:
        return False
