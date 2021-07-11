# Dynamic Programming

## Chapter terms

### `Dynamic programming`

* [`Dynamic programming (DP)`](https://en.wikipedia.org/wiki/Dynamic_programming): an algorithmic technique for solving an *optimization* problem by breaking it down into simpler *subproblems* and utilizing the fact that the *optimal* solution to the overall problem depends upon the optimal solution to its subproblems.

  This algorithm only works when each subproblem is *discrete* such that none of the subproblems are *dependent* on each other. However, in the case of *non-discrete* subproblems, we should use the **greedy algorithm**.

  Each discrete subproblem can be further broken down into its own set of discrete *sub*-subproblems.

[The knapsack problem](https://en.wikipedia.org/wiki/Knapsack_problem) (revisited) - recall that the simple solution to this problem is to generate every possible set of goods to fit into the knapsack, then find the set that is the most valuable. The problem with this algorithm is that it takes `O(2^n)` time (this is *incredibly* slow).

However, we learned how to come up with an *approximate* solution in [Chapter 8](../8_greedy-algorithms/README.md). But, what if we still want to calculate the *optimal* solution? We will need to use **dynamic programming**.

Continuing with the knapsack problem, we solve it by solving the problem for *smaller* knapsacks and then working up to solving the entire problem. We use **dynamic programming** to solve this problem by starting with a grid (imagine it has vertical lines):

  | *Item* | **1 lb** | **2 lbs** | **3 lbs** | **4 lbs** |
  | --- | --- | --- | --- | --- |
  | Guitar | | | | |
  | Stereo | | | | |
  | Laptop | | | | |

This grid represents the *sub-knapsacks* (smaller knapsacks) that we will use to break down the entire problem. Each column is a knapsack with its maximum carrying capacity ranging from 1 lb to 4 lbs and each row is an item.

Recall the weight and value of each item below:

| Item | Weight (lbs) | Value ($) |
| --- | --- | --- |
| Guitar | 1 lb | $1,500 |
| Stereo | 4 lbs | $3,000 |
| Laptop | 3 lbs | $2,000 |
| iPhone | 1 lb | $2,000 |
| MP3 Player | 1 lb | $1,000 |

Now that we have our grid, we will start in the first row and, for each *sub-knapsack*, decide if we will take the item: does the item fit in the sub-knapsack? If yes, then take it.

  | *Item* | **1 lb** | **2 lbs** | **3 lbs** | **4 lbs** |
  | --- | --- | --- | --- | --- |
  | Guitar | $1,500 (G) | $1,500 (G)  | $1,500 (G)  | $1,500 (G)  |
  | Stereo | | | | |
  | Laptop | | | | |

For this row, we are only able to take the guitar since it's the only item available at this point in the algorithm. Therefore, it's an easy decision to take it for each sub-knapsack.

In the second row, we can take the stero ***or*** the guitar. So: for each *sub-knapsack*, which item will we take: guitar or stero? Which one(s) can we fit in the sub-knapsack such that we will have the highest available value?

  | *Item* | **1 lb** | **2 lbs** | **3 lbs** | **4 lbs** |
  | --- | --- | --- | --- | --- |
  | Guitar | $1,500 (G) | $1,500 (G)  | $1,500 (G)  | $1,500 (G)  |
  | Stereo | $1,500 (G) | $1,500 (G) | $1,500 (G) | *$3,000 (S)* |
  | Laptop | | | | |

The stero is 4 lbs and means we it only really makes sense to take it for the 4 lb capacity sub-knapsack since it's the only one that it would fit.

Finally, we do the same thing for the laptop row: for each *sub-knapsack*, which item will we take: guitar, stereo, or laptop? Which one(s) can we fit in the sub-knapsack such that we will have the highest available value?

  | *Item* | **1 lb** | **2 lbs** | **3 lbs** | **4 lbs** |
  | --- | --- | --- | --- | --- |
  | Guitar | $1,500 (G) | $1,500 (G)  | $1,500 (G)  | $1,500 (G)  |
  | Stereo | $1,500 (G) | $1,500 (G) | $1,500 (G) | $3,000 (S) |
  | Laptop | $1,500 (G) | $1,500 (G) | *$2,000 (L)* | *$2,000 (L)<br>$1,500 (G)* |

In this row, the 1 lb and 2 lb sub-knapsacks can, predictably, only hold the guitar. However, the 3 lb sub-knapsack increases in value by $500 because we are able to take the laptop. Additionally, the 4 lb sub-knapsack increases in overall value by $500 because we can combine the guitar ***and*** the laptop in this sub-knapsack. Here's the algorithm we used in this example:

    cell[i][j] = max of {1. The previous max(value at cell[i-1][j])
                        {2. Value of current item + value of the remaining space (cell[i-1][j-(item's weight)])

Adding a new value is easy because all we need to do is add another row to our grid and then continue accumulating the total like we did before.

  | *Item* | **1 lb** | **2 lbs** | **3 lbs** | **4 lbs** |
  | --- | --- | --- | --- | --- |
  | Guitar | $1,500 (G) | $1,500 (G)  | $1,500 (G)  | $1,500 (G)  |
  | Stereo | $1,500 (G) | $1,500 (G) | $1,500 (G) | $3,000 (S) |
  | Laptop | $1,500 (G) | $1,500 (G) | $2,000 (L) | $2,000 (L)<br>$1,500 (G) |
  | iPhone | *$2,000 (I)* | *$2,000 (I)<br>$1,500 (G)* | *$2,000 (I)<br>$1,500 (G)* | *$2,000 (I)<br>$2,000 (L)* |

***Changing the order of the rows will not affect the final answer.***

The concept of **dynamic programming** is:

* Useful when you're trying to optimize something with a given constraint.
* When the problem you're trying to solve can be broken down into discrete subproblems such that each subproblem is independent.

In general:

* Every **dynamic programming** programming solution involves a `grid`.
* The values in each cell typically represent what you're trying to optimize.
* Each cell represents a subproblem where each axis are discrete constraints.

### `Longest common substring`

* [`Longest common substring`](https://en.wikipedia.org/wiki/Longest_common_substring_problem): a computer science problem where the objective is to find the *longest* string that is a *substrint* of *two or more* strings.

  This problem can be applied to other problems like [data deduplication](https://en.wikipedia.org/wiki/Data_deduplication) and [plagiarism detection](https://en.wikipedia.org/wiki/Plagiarism_detection).

For this problem, we need to understand what the objective is, the value of each cell in the grid, how to divide the problem into subproblems, and what the axes are of the grid.

Suppose a user enters the search term "`hish`" and one of the suggested terms is "`fish`". How do we divide this problem into subproblems? The subproblems could be comparing each letter of each term and totaling the counts for each substring (cell). Therefore, our grid would look like this:

| *Letters* | H | I | S | H |
| --- | --- | --- | --- | --- |
| **F** | | | | |
| **I** | | | | |
| **S** | | | | |
| **H** | | | | |

Unfortunately, no there are no hard and fast rules on how to apply **dynamic programming** to *any* problem. It requires experimentation, patience, and tenacity.

We want to go down each row and count the number of times we had a letter match. After each subsequent row, we will total the previous row. The first row will look like this:

| *Letters* | H | I | S | H |
| --- | --- | --- | --- | --- |
| **F** | *0* | *0* | *0* | *0* |
| **I** | | | | |
| **S** | | | | |
| **H** | | | | |

Now, we do the same thing with the second row and increment the value of the *diagonal* by 1 if we found another match from the previous row. Therefore, a completed grid for this problem will look like the grid below:

| *Letters* | H | I | S | H |
| --- | --- | --- | --- | --- |
| **F** | 0 | 0 | 0 | 0 |
| **I** | 0 | *1* | 0 | 0 |
| **S** | 0 | 0 | *2* | 0 |
| **H** | 0 | 0 | 0 | *3* |

What if we wanted to figure out which words that match the closest? Then, we would be looking for the **longest common subsequence**. This is when we count the *total* number of matching letters between two words.

### Conclusion

Applications of **dynamic programming**:

* Calculating the longest common subsequence to find similarities in DNA strangs.
* A `diff` function (like `git diff`) uses dynamic programming to show the differences between two files.
* The *Levenshtein distance* is a similarity measure between two strings that uses dynamic programming. This measure is used for things like spell-check and identifying copyrighted data.
* Features like *word wrap* use dynamic programming.
