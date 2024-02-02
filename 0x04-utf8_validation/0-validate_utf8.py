#!/usr/bin/python3
"""moduel for utf validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """validating utf8
    Keyword arguments:
    data: data to avlidate
    Return: bytes
    """
    bts = 0
    for byte in data:
        if bts:
            if byte >> 6 == 0b10:
                bts -= 1
            else:
                return False
        else:
            if byte >> 7 == 0:
                bts = 0
            elif byte >> 5 == 0b110:
                bts = 1
            elif byte >> 4 == 0b1110:
                bts = 2
            elif byte >> 3 == 0b11110:
                bts = 3
            else:
                return False
    return bts == 0
