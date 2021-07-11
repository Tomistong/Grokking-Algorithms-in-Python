#!/usr/bin/env python


def longest_common_subsequence(X:str, Y:str, m:int, n:int):
    '''Simple function solution to the longest common substring problem.'''
    # Initialize dynamic programming grid
    grid = [[0 for i in range(m)] for j in range(n)]
    
    # Base case
    if m == 0 or n == 0:
        return grid
    
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                grid[i][j] = grid[i - 1][j - 1] + 1
            else:
                grid[i][j] = max(
                    grid[i - 1][j],
                    grid[i][j - 1]
                )
    
    return grid

X = 'fosh'
Y = 'fish'
m = len(X)
n = len(Y)
print(longest_common_subsequence(X, Y, m, n))