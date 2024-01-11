#!/usr/bin/python3
"""module for lockboxes"""


def canUnlockAll(boxes):
    """lockbox
    Keyword arguments:
    boxes: list with box of keys
    Return: true or false
    """
    unlocked = [0]

    for id, box in enumerate(boxes):
        if not box:
            continue
        for Key in box:
            if Key < len(boxes) and Key not in unlocked and Key != id:
                unlocked.append(Key)
    if len(unlocked) == len(boxes):
        return True
    return False
