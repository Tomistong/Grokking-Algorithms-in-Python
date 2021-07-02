#!/usr/bin/env python

def simple_search(l:list, item):
    """Perform simple search on a homogenous list for an item and return it's 
    location.

    Args:
        l (list): the homogenous list to be searched
        item (): the item to look for in the list

    Returns:
        int: index location of item in list or `None`
    """
    
    i = 0
    max_len = len(l) - 1
    # Cut `l` in half until `item` is found
    while i <= max_len:
        guess = l[i]
        if guess == item:
            # Item was found
            return i
        else:
            # Guess is too low
            i += 1
    return None


l1 = [1, 3, 5, 7, 9]
l2 = ['a', 'b', 'c', 'd', 'e', 'f']
l3 = [{'a':1}, {'b':2}, {'c':3}]
l4 = [1, 'a', 'b', 'c', 3, 9,  'd', 5, 7, 'e', 'f']

print(simple_search(l1, 3))     # => 1
print(simple_search(l1, -1))    # => None
print(simple_search(l2, 'b'))   # => 1
print(simple_search(l2, 'z'))   # => None
print(simple_search(l3, {'c':3}))   # => 2
print(simple_search(l4, 'c'))   # => ERROR