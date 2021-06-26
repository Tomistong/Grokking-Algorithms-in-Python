from random import randint


def quicksort(l:list, is_random:bool=False):
    if len(l) < 2:
        return l
    else:
        pivot_idx = 0 if not is_random else randint(0, len(l)-1)
        pivot = l[pivot_idx]
        less = [i for i in l[1:] if i <= pivot]
        greater = [i for i in l[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


l0 = [10, 5, 2, 3]
l1 = [5, 9, 7, 1, 3]
l2 = ['a', 'c', 'e', 'f', 'b', 'd']

print(quicksort(l0))
print(quicksort(l1))
print(quicksort(l2))
print(quicksort(l0, is_random=True))
print(quicksort(l1, is_random=True))
print(quicksort(l2, is_random=True))