#!/usr/bin/python3

"""Creates the Pascal's triangle"""

def pascal_triangle(n):
    """A function that generates the pascal's triangle
	
    Args:
        n (int): the number to use for printing

    Returns:
        A trinagle of lists
    """

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            previous_row = triangle[-1]
            new_row = [1]

            for j in range(1, i):
                new_row.append(previous_row[j - 1] + previous_row[j])
            new_row.append(1)
            triangle.append(new_row)
    return triangle    
