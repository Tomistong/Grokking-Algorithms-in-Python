# Hash Tables

## Chapter terms

* `Hash tables`: a data structure (e.g. array) made up of values mapped using a mapping function, or **hash function**, such that providing the **hash function** returns the exact address of the corresponding value. Python has it's own version of this called `dictionaries`. On *average*, a **hash table** takes `O(1)` (*constant time*) for everything. In the *worst* case, a **hash table** takes `O(n)` time.

  Below is a simple example of a Python **hash table**: a *dictionary*:

  ```python
  >>> example = dict()
  >>> example['a'] = 1
  >>> example['b'] = 2
  >>> example['c'] = 3
  >>> print(example)
  {'a': 1, 'b': 2, 'c': 3}
  ```

  A **hash function** is used to map values to an address in the data structure from an input (the *key*). Therefore, by providing the *key* to the same **hash function**, we can *instantly* find *any* value in the table.

  You can't have duplicate keys in a hash table since it would break the hash table. This is called a **collision** and is not allowed in hash tables.

  Comparison table of **hash tables**, **arrays**, and **linked lists**:

  | Operation | Hash Tables (average) | Hash Tables (worst) | Arrays | Linked Lists |
  | --- | --- | --- | --- | --- |
  | Search | `O(1)` | `O(n)` | `O(1)` | `O(n)` |
  | Insert | `O(1)` | `O(n)` | `O(n)` | `O(1)` |
  | Delete | `O(1)` | `O(n)` | `O(n)` | `O(1)` |

  We can avoid the *worst* case (and guarantee the *average* case) by ensuring our **hash table** doesn't have any collisions such that the **hash table** has:

    * A low **load factor**
    * A good **hash function**

  In general, **collisions**, **load factor**, and **hash functions** aren't things we need to worry about since most modern programming languages have their own implementation of **hash tables** (ex: Python dictionaries). We can assume these data types have been optimized for good performance and will not be plagued by issues mentioned here.

  **Hash tables** are good for:
  * catching duplicates
  * caching data (like web pages)
  * modeling relationships
  * applications that need a fast data structure

* `Hash functions`: a special type of function that takes a string (or any data type) as an input and outputs a number. When used with a **hash table**, however, it points to the address of that string (key). Therefore, a **hash function** maps strings to numbers.

  1. The **hash function** needs to be consistent. For example, the string "`apple`" should always return "`4`". Otherwise, the **hash table** would break.

  2. The **hash function** needs to map different words to different numbers. For example, "`pear`" should not return "`4`" since that is already mapped to "`apple`".

  A *good **hash function*** will distribute values evenly across the array. However, a *bad **hash function*** will group values together, resulting in at least one **collision**. An example of a *good **hash function*** is the ["SHA" function](https://en.wikipedia.org/wiki/SHA-1).

* `Collisions`: when two different keys are mapped by the **hash function** to the same address in the **hash table**

  **Collisions** can be avoided by, for example, using the first letter of the key to categorize the keys across 26 slots where each slot is made up of a linked list of the full key to it's corresponding value.

  Ideally, the **hash function** evenly maps all keys over the **hash table**. Using a linked list in a shared slot on the **hash table** is one way to avoid **collisions**, but is no substitute for a good **hash function**.

* `Load factor`: the measure of items in a **hash table** out of the total number of available slots in the array. That is:

  ![number of items in hash table / total number of slots](http://www.sciweavers.org/tex2img.php?eq=%5Cfrac%7B%5Ctext%7Bnumber%20of%20items%20in%20hash%20table%7D%7D%7B%5Ctext%7Btotal%20number%20of%20slots%7D%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)
  
  Since **hash tables** use arrays for storage, the **load factor** is used to calculate proportion of usage. It's possible to have a **load factor** greater than `1`, however. Having a **load factor** greater than `1` tells us that the **hash table** is overloaded and it needs to be *resized* by adding more slots to array. Having a load factor below `1` means the performance of the **hash table** will tend towards `O(1)` time.
