#!/usr/bin/env python

'''
Input:
    Values: stored in array `val` ($)
    Weights: stored in array `wt` (lbs)
    Number of distinct items: `n` (#)
    Knapsack capacity: `W` (lbs)

0: guitar
1: stereo
2: laptop
3: iPhone
4: mp3 player
'''


def knapsack(W, wt, val, n):

    # Base case
    if n == 0 or W == 0:
        return 0
    
    # If weight of item is more than capacity, exclude from optimal solution
    if (wt[n-1] > W):
        return knapsack(W, wt, val, n-1)
    # Return max of 2 cases:
    #   (1): nth item included
    #   (2): not included
    else:
        return max(
            val[n-1] + knapsack(W-wt[n-1], wt, val, n-1),
            knapsack(W, wt, val, n-1)
        )


# Book example constraints
val = [1500, 3000, 2000, 2000, 1000]
wt = [1, 4, 3, 1, 1]
W = 15
n = len(val)
print(knapsack(W, wt, val, n))

# Online (geeksforgeeks.org) example constraints
# https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/
val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapsack(W, wt, val, n))