# Selection Sort

## Chapter terms

* `Arrays`: a *contiguous* list of elements in memory.

If the next unit of memory directly after the last element of the **array** is occupied and we need to add an element to the **array**, we would need to reassign the entire **array** to a *new* place in memory. One way around this problem is to request more units of memory than the entire length of the **array** in order to mitigate the issue presented in the previous sentence. However, if we don't use those units of memory, they'll be wasted when something else could have used that memory. Additonally, if we need to add more elements than the extra units we reserved, we're back to square one and have to move the entire **array**!

The advantage of **arrays** is that we know the address of every item. For example, suppose we have an **array** of 10 items and we want to read item # 10. To read item # 10, all we have to do is reference it's index, `09`.

**Arrays** can do both [**sequential access**](#types-of-access) *and* [**random access**](#types-of-access).

* `Linked lists`: a *non-contiguous* list of elements in memory such that each element stores the address of the next item in the list.

As you traverse the **linked list**, the current item tells you the location (in memory) of the next item in the list. Adding an item to a **linked list** doesn't suffer from the same problem as an array either - we just put the additional item anywhere in memory that's free and store the address with the previous item.

However, **linked lists** present a new problem: what if we want to read the last item in the list? We can just travel to the end of the list, we have to read each item in succession to find the address of the following item. For example, if we have a **linked list** of 10 items and want to read the last item, we have to start with item #1 to get the address of item #2, and so on.

**Linked lists** can *only* do [**sequential access**](#types-of-access).

* `Selection sort`: a *sorting* algorithm that loops over a list of `n` element `n` times and returns a sorted list of elements (ascending/descending).

The **selection sort** algorithm takes ![O(n^2)](http://www.sciweavers.org/tex2img.php?eq=O%28n%5E%7B2%7D%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0) time.

## Arrays versus Linked Lists

### Comparison of Operation Types

Operation | Arrays | Linked Lists
--- | --- | ---
Insert | Good - if there is available contiguous memory | Good - order can be preserved, memory does not need to be contiguous
Insert | Bad - if no contiguous memory is available |
Delete | Good - these always work | Good - these always work
Read | Good - you know the address of every item | Bad - you need to start at the beginning for any item

### Comparison of Operation Times

Operation | Arrays | Linked Lists
--- | --- | ---
Insert | O(1) | O(n)
Delete | O(n) | O(1)
Read | O(n) | O(1)

## Types of Access

* **Random access**: read elements in any order.

* **Sequential access**: reading elements one by one, starting at the beginning.
