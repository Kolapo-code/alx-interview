#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] if i == 0 else [1, 1]
        if i >= 2:
            for j in range(1, i):
                row.insert(j, triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(row)

    return triangle

# Test the function
n = 5
result = pascal_triangle(n)
for row in result:
    print(row)
