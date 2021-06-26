# Hash Tables

## Chapter terms

* `Hash tables`: a data structure (e.g. array) made up of values mapped using a mapping function, or **hash function**, such that providing the **hash function** returns the exact address of the corresponding value. Python has it's own version of this called `dictionaries`.

  ```python
  >>> example = dict()
  >>> example['a'] = 1
  >>> example['b'] = 2
  >>> example['c'] = 3
  >>> print(example)
  {'a': 1, 'b': 2, 'c': 3}
  ```

The **hash function** is used to map the values to their address in the data structure. Therefore, we can use that same function to find the value by computing the address with the function when we need to run a search.

**Hash tables** are useful for when you need to map one thing to another thing or look something up.

You can't have duplicate keys in a hash table since it would break the hash table. This is called a **collision** and is not allowed in hash tables.

* `Hash functions`: a special type of function that takes a string (or any data type) as an input and outputs a number. When used with a **hash table**, however, it points to the address of that string (key). Therefore, a **hash function** maps strings to numbers.

  1. The **hash function** needs to be consistent. For example, the string "`apple`" should always return "`4`". Otherwise, the **hash table** would break.

  2. The **hash function** needs to map different words to different numbers. For example, "`pear`" should not return "`4`" since that is already mapped to "`apple`".

* `Collisions`: when two different keys are mapped by the **hash function** to the same address in the **hash table**

**Collisions** can be avoided by, for example, using the first letter of the key to categorize the keys across 26 slots where each slot is made up of a linked list of the full key to it's corresponding value.

Ideally, the **hash function** evenly maps all keys over the **hash table**. Using a linked list in a shared slot on the **hash table** is one way to avoid **collisions**, but is no substitute for a good **hash function**.
