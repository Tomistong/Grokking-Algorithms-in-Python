def binary_search(l:list, item):
    """Perform binary search on a homogenous list for an item and return it's 
    location.

    Args:
        l (list): the homogenous list to be searched
        item (): the item to look for in the list

    Returns:
        int: index location of item in list or `None`
    """
    low = 0
    high = len(l) - 1
    # Cut `l` in half until `item` is found
    while low <= high:
        mid = (low + high)
        guess = l[mid]
        if guess == item:
            # Item was found
            return mid
        if guess > item:
            # Guess is too high
            high = mid - 1
        else:
            # Guess is too low
            low = mid + 1
    return None


l1 = [1, 3, 5, 7, 9]
l2 = ['a', 'b', 'c', 'd', 'e', 'f']
l3 = [{'a':1}, {'b':2}, {'c':3}]
l4 = [1, 'a', 'b', 'c', 3, 9,  'd', 5, 7, 'e', 'f']

print(binary_search(l1, 3))     # => 1
print(binary_search(l1, -1))    # => None
print(binary_search(l2, 'b'))   # => 1
print(binary_search(l2, 'z'))   # => None
print(binary_search(l3, {'c':3}))   # => 2
print(binary_search(l4, 'c'))   # => ERROR