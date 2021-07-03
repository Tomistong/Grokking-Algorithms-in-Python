# Greedy Algorithms

## Chapter terms

* `Greedy algorithm`: an algorithm used in **NP-complete problems** such that *at each step you pick the locally optimal solution*. These algorithms don't always find the *perfect* or *best* solution, but this is the trade-off when using this simple algorithm.

      Suppose we have a commercial that we want to on all televesions in all 50 states, but it costs money to have the local television stations run your commercial. We need to *minimize* the number of television stations we have play our commercial. Each television station covers a region in the United States, and some overlap with one another.

      How do we find the smallest set of television stations we can have broadcast our commercial to cover all 50 states?

      1. List every possible subset of television stations. This is called the power set and there are 2^n possible subsets.
      2. From this list, pick the set with the least number of television stations such that the set covers all 50 states.

  The problem with the example above is the time it would take to calculate every possible subset of television stations: `O(2^n)` time. This is due to the fact that there are `2^n` stations. This is where **approximation algorithms** come in.

  This is how an approximation algorithm would work for this example:

  1. Pick the television station that covers the most stations that have not yet been covered, even if there's still some overlap.
  2. Repeat step `1` until all 50 states have been covered.

  The new solution will run in `O(n^2)` time which is much faster than finding the *optimal* solution.

* `NP-complete problems`: a type of problem that requires every possible solution to be calculated before finding the optimal/best solution. Alternatively, it is any class of computational problems for which no efficient solution algorithm has been found.

  The **NP** stands for *nondeterministic polynomial*.

  Two examples of **NP-complete** problems:

  1. [The traveling salesperson](https://en.wikipedia.org/wiki/Travelling_salesman_problem).
  2. The set covering problem from earlier.

### How do we identify **NP-complete** problems?

* Your algorithm runs quickly with a handful of items but slows down as the number of items increases.
* Needing to find "all combinations of X" before finding the solution or breaking it down into smaller sub-problems.
* The problem involves a sequence and it's difficult to solve.
* The problem involves a set and it's difficult to solve.
* If the problem can be restated as a set-covering problem or the traveling salesperson problem.
