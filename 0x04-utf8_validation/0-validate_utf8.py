#!/usr/bin/python3
"""moduel for utf validation"""
from typing import List


def validUTF8(data: List[int]) -> bool:
    """validating utf8
    Keyword arguments:
    data: data to avlidate
    Return: bytes
    """

    count = 0
    for byte in data:
        byte &= 0xFF
        if count == 0:
            if byte <= 0x7F:
                count = 0
            elif byte <= 0xDF:
                count = 1
            elif byte <= 0xEF:
                count = 2
            elif byte <= 0xF4:
                count = 3
            else:
                return False
        else:
            if byte >> 6 != 2:
                return False
            count -= 1
    return count == 0
