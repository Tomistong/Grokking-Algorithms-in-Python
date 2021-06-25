# Quicksort

## Chapter terms

* `Divide and conquer (D&C)`: a strategy for determining the *base* case and the *recursive* case in order to develop a *recursive* algorithm.

How to solve a problem using **D&C**:

1. Identify the *base* case (i.e. the simplest possible case).
2. Divide or decrease the problem until it becomes the *base* case.

Suppose we had a plot of land 1,680 meters by 640 meters that we want to divide evenly into *squares*. The base case would be if (1) either side of the plot was a multiple of the other side. That is, if one side was `x` and the other side was `mx`, then we would have `m` squares. So, what would be the *recursive* case?

According to **D&C**, each recursive call needs to reduce the problem. The biggest boxes we can make with our plot are 640m by 640m, but this leaves us with an uneven third square. What if we applied the recursive algorithm to this third, uneven square? WHAT?!

Now, our new problem is to a find the biggest square of the leftover 640m by 400m plot. We reduced our initial problem from 1,680m by 640m to 640m by 400m! [*This problem is an example of Euclid's algorithm*](https://en.wikipedia.org/wiki/Euclidean_algorithm). Therefore, if we find the biggest square that works for our "leftover" plot, then we will have the biggest square that will work for the ***entire*** plot. If we continue with the same strategy of finding the biggest square on successive plots we end up with our *base* case: 160m by 80m == 2 * 80m by 80m.

An 80m by 80m square can evenly divide our ***entire*** plot of 1,680m by 640m into 168 squares.

Another example would be an algorithm to sum any given array of numbers. The *base* case would be an array of 0 or 1 element. Therefore, our objective should be to figure out how we can *recurse* our problem down such that we arrive at the base case. For this example, we would want to take the first element from the array and add it to the sum of the remaining array. But, what if we apply the same operation on the remaining array? Eventually, this will lead us to the base case where at the top of the *stack* would be an array of 0. Then, we would follow the stack back down adding each number returned to the previous result.

* `Quicksort`: a commonly used sorting algorithm that sorts arrays by partitioning an array into smaller arrays such that larger/smaller elements are on ascending/descending.

The **quicksort** algorithm works by using *recursion* by breaking the problem down into smaller problems so each of the results can be combined to get the final result.

This is how it works:

1. The algorithm picks a *pivot* element.
2. Partition the array into two sub-arrays: elements less than the *pivot* and elements greater than the *pivot*.
3. Call **quicksort** recursively on the two sub-arrays.

The *pivot* chosen for the **quicksort** algorithm is what determines the actual Big O speed. In the *average* ***and*** *best* case, **quicksort** takes `O(n*log(n))` time. In the *worst* case, **quicksort** takes `O(n^2)` time. However, the **merge sort** algorithm is *always* `O(n*log(n))`.

When we say something is "`O(n)` time", we mean:

    c * n

Where `c` is some constant amount of time. This constant could be 10 milliseconds, 1 second, 100 minutes, whatever. In most cases, this constant is ignored as it doesn't make a difference on the outcome. However, when it comes to **quicksort** versus **merge sort**, it *does* make a difference.

**Quicksort** has a smaller constant that **merge sort** and is faster in practice because it tends towards the *average* (*best*) case more often than the *worst* case.

    "If you always choose a random element in the array as the pivot, quicksort will complete in `O(n*log(n))` time on average."
