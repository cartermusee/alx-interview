#!/usr/bin/python3

""" stdin and computes metrics """
import sys


def printStatus(dic, size):
    """ Prints file size """
    print("File size: {:d}".format(size))
    for i in sorted(dic.keys()):
        if dic[i] != 0:
            print("{}: {:d}".format(i, dic[i]))


statusCodes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
               "404": 0, "405": 0, "500": 0}

ct = 0
size = 0

try:
    for line in sys.stdin:
        if ct != 0 and ct % 10 == 0:
            printStatus(statusCodes, size)

        lt = line.split()
        ct += 1

        try:
            size += int(lt[-1])
        except Exception:
            pass

        try:
            if lt[-2] in statusCodes:
                statusCodes[lt[-2]] += 1
        except Exception:
            pass
    printStatus(statusCodes, size)


except KeyboardInterrupt:
    printStatus(statusCodes, size)
    raise