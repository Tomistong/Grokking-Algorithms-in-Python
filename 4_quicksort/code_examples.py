#!/usr/bin/env python

def recursive_array_addition(l:list):
    """Sum an array of integers using recursion."""
    if len(l) == 0:
        return 0
    else:
        i = l.pop()
        return i + recursive_array_addition(l)

print(recursive_array_addition([2, 4, 6]))
print(recursive_array_addition([5, 6, 7]))


def recursive_array_count(l:list):
    """Count an array of elements using recursion."""
    if l == []:
        return 0
    else:
        l.pop()
        return 1 + recursive_array_count(l)

print(recursive_array_count([1, 2, 3]))
print(recursive_array_count([1, 1, 1, 1, 1]))


def recursive_array_max(l:list):
    """Find the max element using recursion."""
    if len(l) < 2:
        return 0 if len(l) == 0 else l[0]
    else:
        i = l.pop()
        return i if i > max(l) else recursive_array_max(l)

print(recursive_array_max([2, 4, 6]))
print(recursive_array_max([6, 4, 2]))


def recursive_binary_search(l:list, item):
    """Use binary search with recursion."""
    if len(l) < 2:
        return 0 if len(l) == 1 and item == l[0] else None
    else:
        mid = len(l) // 2
        if item == l[mid]:
            return mid
        elif item > l[mid]:
            return recursive_binary_search(l[mid:], item)
        else:
            return recursive_binary_search(l[:mid], item)

l1 = [1, 3, 5, 7, 9]
l2 = ['a', 'b', 'c', 'd', 'e', 'f']

print(recursive_binary_search(l1, 3))     # => 1
print(recursive_binary_search(l1, -1))    # => None
print(recursive_binary_search(l2, 'b'))   # => 1
print(recursive_binary_search(l2, 'z'))   # => None