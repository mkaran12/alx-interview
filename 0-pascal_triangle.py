#!/usr/bin/python3
"""Triangle Triangle"""


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # First row is always [1]
    
    for i in range(1, n):
        prev_row = triangle[i - 1]
        new_row = [1]  # Start with 1
        
        # Fill the row based on the previous row
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])
        
        new_row.append(1)  # End with 1
        triangle.append(new_row)

    return triangle
