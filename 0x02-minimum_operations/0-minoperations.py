#!/usr/bin/python3
"""
Script that computes a minimum operations
needed in a CopyAll - Paste task
"""


def minOperations(n):
    if n == 1:
        return 0  # Already have 1 H character

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)

    if operations[n] == float('inf'):
        return 0  # It's impossible to achieve n H characters
    else:
        return operations[n]

# Example usage:
n = 9
result = minOperations(n)
print(f"Number of operations to achieve {n} H characters: {result}")
