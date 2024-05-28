#!/usr/bin/python3



def pascal_triangle(n):
    """Define the pascal triangle
    
    Args:
        n (int): number of rows 
    """
    if n <=0:
        return []
    triangle = [[1]]
    for cpt in range(1, n):
        line = [1]
        for cpt_items in range(1, cpt):
            line.append(triangle[cpt-1][cpt_items-1] + triangle[cpt-1][cpt_items])
        line.append(1)
        triangle.append(line)
    return triangle
