# Dijkstra's Algorithm

## Chapter terms

Suppose we have a similar problem as before: we want to get from point A to point B and this problem is represented by a **graph**. Previously, our solution to this problem would be to find the *shortest* path consisting of the *least number of node connections*. We can find this path using **breadth-first search**.

However, suppose in this same problem we added distance, or travel time, between each of the nodes: which path is faster/shorter? Is the same path we already chose fastest/shortest? This is where **Dijkstra's algorithm** comes in.

* `Dijkstra'a algorithm`: a *searching* algorithm that finds the shortest ***weighted*** distance between two *things*.

  * Note: **Dijkstra's algorithm** *only* works with *directed acyclic **graphs*** (DAGs) such that the weights are `>= 0`. In other words: a directed **graph** that is not a cycle where the weights are non-negative.

  There are four steps to Dijkstra's algorithm:

  1. Find the "cheapest" node. This is the node you can get to in the least amount of time/distance.
  2. Check whether there's a cheaper path to the neighbors of this node. If so, update their costs (cumulative total time/distance from where you started).
  3. Repeat until you've done this for every node in the **graph**.
  4. Calculate the final path.

  A *weighted* **graph** is a **graph** where each *edge* has a value associated with it - these are the *weights*.

  Remember: **Dijkstra's algorithm** isn't about finding the *literal shortest* path, in terms of distance. It could mean the *minimal measure* of any other thing between two points. It may also be helpful to think of this algorithm as a *cost minimization* algorithm.

* `Weighted graph`: a **graph** *without* weights.

* `Unweighted graph`: a **graph** *with* weights.

* `Cycle`: a **graph** where the starting node is connected to itself either directly or indirectly.

* `Bellman-Ford algorithm`: a *searching* algorithm that finds the shortest ***weighted*** distance between two *things* such that the weights can be any *real-valued* number (`-infinity < n < +infinity`).
