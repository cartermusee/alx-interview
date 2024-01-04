#!/usr/bin/python3

# module for creating pascal triangle
def pascal_triangle(n):
    """
    function itself
    args:
        n: the number
    Return: triangle or 0
    """
    
    if n <= 0:
        return 0
    else:
        rectangle = []
        for i in range(n):
            row = [1] * (1 + i)
            for j in range(1, i):
                row[j] = rectangle[i-1][j-1] + rectangle[i-1][j]
            rectangle.append(row)
        return rectangle

