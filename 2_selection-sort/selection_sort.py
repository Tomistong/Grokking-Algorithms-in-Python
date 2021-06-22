def find_smallest(arr):
    """Return the address of the smallest element in an array.

    Args:
        arr: a Python iterable

    Returns:
        int: index of the smallest element
    """
    # Store the first element and assume it's the smallest
    smallest = arr[0]
    smallest_index = 0
    # Loop over every element in the array
    for i in range(1, len(arr)):
        # Check if the new element from the array is smaller
        if arr[i] < smallest:
            # Update the 'smallest' variables
            smallest = arr[i]
            smallest_index = i
    # Return the address of the smallest element from the array
    return smallest_index


def find_biggest(arr):
    """Return the address of the biggest element in an array.

    Args:
        arr: a Python iterable

    Returns:
        int: index of the biggest element
    """
    # Store the first element and assume it's the biggest
    biggest = arr[0]
    biggest_index = 0
    # Loop over every element in the array
    for i in range(1, len(arr)):
        # Check if the new element from the array is bigger
        if arr[i] < biggest:
            # Update the 'biggest' variables
            biggest = arr[i]
            biggest_index = i
    # Return the address of the biggest element from the array
    return biggest_index


def selection_sort(arr, asc:bool=True):
    """Perform selection sort (ascending/descending) on a homogenous array 
    and return a sorted array.

    Args:
        arr: a Python iterable
        asc (bool, optional): sort the array ascending (default) or descending

    Returns:
        new_array: a sorted array ascending or descending
    """
    # Create empty array to store results
    new_array = []
    # Loop over every element in the array
    for _ in range(len(arr)):
        # Get the address of the smallest/biggest element
        i = find_smallest(arr) if asc else find_biggest(arr)
        # Append the element from the array and remove it
        new_array.append(arr.pop(i))
    # Return sorted array
    return new_array



print(selection_sort([5, 3, 6, 2, 10]))