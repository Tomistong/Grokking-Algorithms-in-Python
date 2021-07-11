#!/usr/bin/env python


def longest_common_substring1(X:str, Y:str, m:int, n:int):
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
            
    return grid


def longest_common_substring2(X:str, Y:str, m:int, n:int, count=0):
    '''
    Find the length of the longest common substring of 2 strings.

    Input:
        X (str): one of the strings to analyze
        Y (str): the other string to analyze
        m (str): length of string `X` (`m` rows)
        n (str): length of string `Y` (`n` columns)

    Output:
        result (int)
    '''
    # Base case
    if m == 0 or n == 0:
        return count
    
    # Check if there is a match
    if X[m - 1] == Y[n - 1]:
        count = longest_common_substring2(
            X,
            Y,
            m - 1,
            n - 1,
            count + 1
        )
    
    # Get the maximum count of letters in the substring
    count = max(
        count,
        max(
            longest_common_substring2(X, Y, m, n - 1, 0),
            longest_common_substring2(X, Y, m - 1, n, 0)
        )
    )
    return count

# Geeksforkeegs.org example
# https://www.geeksforgeeks.org/longest-common-substring-dp-29/
# Fails with non-alphanum characters
X = "abcdxyz"
Y = "xyzabcd"
m = len(X)
n = len(Y)
print(longest_common_substring2(X, Y, m, n, 0))
X = "abcdxyz"
Y = "xyzabcd"
m = len(X)
n = len(Y)
print(longest_common_substring1(X, Y, m, n))
X = 'hish'
Y = 'fish'
m = len(X)
n = len(Y)
print(longest_common_substring1(X, Y, m, n))
X = 'vista'
Y = 'hish'
m = len(X)
n = len(Y)
print(longest_common_substring1(X, Y, m, n))
X = 'fosh'
Y = 'fort'
m = len(X)
n = len(Y)
print(longest_common_substring1(X, Y, m, n))
X = 'fosh'
Y = 'fish'
m = len(X)
n = len(Y)
print(longest_common_substring1(X, Y, m, n))