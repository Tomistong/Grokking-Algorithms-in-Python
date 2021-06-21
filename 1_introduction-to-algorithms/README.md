# Introduction to Algorithms

## Chapter terms

* `Algorithm`: a set of instructions for accomplishing a task.
* `Big O notation`: a special notation used to illustrate the search rate of an algorithm (the lower the better). That is, given an algorithm of ![O(n)](http://www.sciweavers.org/tex2img.php?eq=O%28n%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0), we plug in the size of the list (or, *estimated* size) for `n` to better understand the maximum number of **steps** it could take for the algorithm to complete. The **O** in the notation stands for *operations*, which means it tells us the maximum number of *operations* an algorithm will take to complete it's search.

Suppose the element you're looking for in a **simple search** is the first element. This doesn't mean the algorithm takes `O(1)` operations to complete it's search, rather, this is a just a *best-case* scenario. Again, however, Big O notation tells you the *worst-case* scenario number of operations the algorithm will take. One way to better understand could be to assume 10 operations can be performed every one second. Therefore, you can use this as a general rule of thumb to see which algorithm has the fastest worst-case.

Here are some other common Big O run times:

* ![O(log_2n)](http://www.sciweavers.org/tex2img.php?eq=O%28%5Clog_2n%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
  * Name: *log time*
  * Example: **Binary search**
* ![O(n)](http://www.sciweavers.org/tex2img.php?eq=O%28n%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
  * Name: *linear time*
  * Example: **Simple search**
* ![O(n*log_2n)](http://www.sciweavers.org/tex2img.php?eq=O%28n%20%2A%20log_2n%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
  * Example: *Quicksort*
* ![O(n^2)](http://www.sciweavers.org/tex2img.php?eq=O%28n%5E%7B2%7D%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
  * Example: *Selection sort*
* ![O(n!)](http://www.sciweavers.org/tex2img.php?eq=O%28n%21%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
  * Example: *Traveling salesperson*

## Binary Search

**Summary**: searching for an item by starting in the *middle* and return where it's located or return `null`.

**Application**: a sorted list of elements (e.g.: lists).

**Big O notation**: ![O(log_2n)](http://www.sciweavers.org/tex2img.php?eq=O%28%5Clog_2n%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

**Notes**: this algorithm only works when your list is in sorted order.

## Simple Search

**Summary**: searching for an item by starting at the *beginning* and traverse the list to the end until the location is returned or `null`.

**Application**: never, apparently.

**Big O notation**: ![O(n)](http://www.sciweavers.org/tex2img.php?eq=O%28n%29&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
