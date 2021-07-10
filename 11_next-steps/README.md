# Next Steps

## Chapter terms

### Binary tree

A **binary tree** is a tree *data structure* in which each node has at most two children referred to as the *left* child and the *right* child.

### Binary search tree (BST)

A **binary search tree** is a rooted **binary tree** whos internal nodes each store a key *greater* than all the keys in the node's *left subtree* and less than those in its *right subtree*.

  Operation | Array | BST |
  --- | --- | ---
  SEARCH | `O(log n)` | `O(log n)`
  INSERT | `O(n)` | `O(log n)`
  DELETE | `O(n)` | `O(log n)`

Searching for an item in a **binary search tree** takes `O(log n)` time, on *average*. However, in the *worst* case, it takes `O(n)` time. This is assuming, also, that the **BST** is *balanced*. If the tree is *imbalanced*, then the performance will tend towards the *worst* case. There are special trees that can balance themselves, however, such as the [red-black tree](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree).

Another downside to **BSTs** is you can't have random access. That is, you can't access any given element in a **BST**, the tree needs to be traversed.

Here are some other advanced data structures similar to **BSTs**:  

* [B-trees](https://en.wikipedia.org/wiki/B-tree)
* [Red-black trees](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
* [Heaps](https://en.wikipedia.org/wiki/Heap_(data_structure))
* [Splay trees](https://en.wikipedia.org/wiki/Splay_tree)

### [Inverted indexes](https://en.wikipedia.org/wiki/Inverted_index)

An **inverted index** is a database index storing a mapping from content, such as words or numbers, to its location in a table, or in a document or set of documents.

This is what is commonly used to build search engines.

### [Fourier transform](https://en.wikipedia.org/wiki/Fourier_transform)

The **Fourier transform** is a mathematical transformation that decomposes functions depending on space or time into functions depending on spatial or temporal frequency.

The **Fourier transform** can be used to separate a song into frequencies, predict earthquakes, and analyze DNA. [It's the algorithm used to encode a song to MP3 format](https://en.wikipedia.org/wiki/MP3#Encoding_and_decoding). [It's even the algorithm that powers the Shazam app to recognize which song is playing](https://www.toptal.com/algorithms/shazam-it-music-processing-fingerprinting-and-recognition).

### Parallel algorithms

The concept of parallelizing your algorithms is a strategy to make our algorithms faster. For example, the **quicksort** algorithm can be *parallelized* to sort an array in `O(n)` time, instead of `O(n log n)` time.

While this *can* make an algorithm run faster, it's not always the case and can depend on several factors, some of which you can control. You need to consider both the overhead of managing the parellelism and load balancing across your CPU cores.

### [MapReduce](https://en.wikipedia.org/wiki/MapReduce)

**MapReduce** is a programming model and an associated implementation for processing and generating big data sets with a parallel, distributed algorithm on a cluster.

The **MapReduce** algorithm is a type of [*distributed algorithm*](https://en.wikipedia.org/wiki/Distributed_algorithm). It's available through the open source tool [Apache Hadoop](https://hadoop.apache.org/).

This algorithm allows us to query tables with trillions of records where a traditional database system (e.g. MySQL) would struggle. However, this is where **MapReduce** is useful: we can use the **MapReduce** algorithm *through* Apache Hadoop to distribute the workload evenly.

Quite simply, this algorithm consists of two ideas: a `map` function and a `reduce` function.

#### [The `map` function](https://en.wikipedia.org/wiki/Map_(parallel_pattern))

A function that takes an array and applies the function to each item in the array. This isn't done in serial, it's done in *parallel*. Meaning, the function is applied to *all* the elements in an array, all at once. For example,

  ```python
  >>> arr1 = [1, 2, 3, 4, 5]
  >>> arr2 = map(lambda x: 2*x, arr1)
  >>> list(arr2)
  [2, 4, 6, 8, 10]
  ```

However, for a function that's more compute intensive, like downloading URLs, this could take some time to run:

  ```python
  >>> def download_page():
    ...
  >>> arr1 = # a list of URLs
  >>> arr2 = map(download_page, arr1) # this is going to take a while
  ```

We solve this problem with [the **reduce** function](#the-reduce-function).

#### [The `reduce` function](https://en.wikipedia.org/wiki/Reduction_Operator)

A function that reduces an array of items down to *one* item. For example,

  ```python
  >>> from functools import reduce
  >>> arr1 = [1, 2, 3, 4, 5]
  >>> reduce(lambda x,y: x+y, arr1)
  15
  ```

In this example, we simply added all the elements together. However, when coupled with the `map` function, it becomes a powerful combination for parallel computing.

### [Bloom filters](https://en.wikipedia.org/wiki/Bloom_filter)

### HyperLogLog
