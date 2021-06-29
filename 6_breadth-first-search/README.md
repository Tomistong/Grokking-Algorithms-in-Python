# Breadth-First Search

## Chapter terms

* `Graphs`: a model consisting of *nodes* connected by *edges* to illustrate relationship(s)/connection(s). In other words, it's a way to model how different things are connection to one another.

  * *Directed*: a type of **graph** where relationships between nodes only go ***one*** way.

  * *Undirected*: a type of **graph** where relationships between nodes can go ***any*** way.

  A **graph** can be expressed using a **hash table**. Order doesn't matter when adding elements to our **hash table** (Python dictionary) - which is a consequence of how the **breadth-first search** algorithm works. This can, also, be deduced inductively by the fact that a Python dictionary, or a **hash table**, has no ordering to it.

* `Neighbor`: the adjacent, connected *node(s)* of a *node* in **graph**.

* `Breadth-first search (BFS)`: a *searching* algorithm that finds the shortest distance between two *things*.

  Usage of the word "things" is done purposefully to illustrate the application diversity of this algorithm:

  * A checkers game AI that calculates the least amount of moves to a win.
  * A spell checker (fewest edits from a misspelling to a real word).
    * READE**D** -> READE**R**
  * The closest gas station.
  * The least number of bus transfers to get from one place to another.

  There are two steps to solving a **shortest-path problem** using the **BFS** algorithm:

  1. Model the problem as a **graph**.
  2. Solve the problem using **breadth-first search**.

  The **BFS (breadth-first search)** algorithm can help answer two types of questions:

  1. [Is there a path from node `A` to node `B`?](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon)
  2. [What is the shorted path from node `A` to node `B`?](https://en.wikipedia.org/wiki/Shortest_path_problem)

  Here's an example of a question of **type 1**: suppose have have a handful of [Karambit Marble Fade](https://csgostash.com/skin/549/Karambit-Marble-Fade) CS:GO skins you want to sell. *Do you have any friends on your Steam Friends list that would buy the skins?* First, make a list of all your friends on Steam. Then, ask each friend if they would like to buy a legitimate Karambit Marble Fade CS:GO skin. What happens if none of your friends want to buy a skin? Now, we ask the friends of our friends if they would like to buy a skin. We proceed through this logic of asking friends, friends of friends, etc. until we find a buyer. This example illustrates how **breadth-first search** works.

  We can use the same example to answer a question of **type 2**: who is the *closest* buyer of our Karambit Marble Fade CS:GO skins? Each time we expanded our search beyond the initial list of friends, we move up to the next *degree*. That is, the friends we have on our Friends list would be the ***first-degree connections***, and *their* friends would be the ***second-degree connections***. Ideally, we would prefer to find a ***first-degree connection*** over a ***second-degree connection*** and a ***second-degree connection*** over a ***third-degree connection***, etc. This is exactly how the **breadth-first search** algorithm works: it starts with the ***first-degree connections*** and expands outward. If we have a skin buyer in both our ***first-degree*** and ***second-degree connections***, we prefer the former since this is a shorter path. This is a data structure called a **queue**.

  Below is a step-by-step guide showing how the **breadth-first search** algorithm will work on this example:

  1. Keep a **queue** containing the people to check.
  2. Pop (**dequeue**) a person (`anon`) off the **queue**.
  3. Check if `anon` is a skin buyer.
  4. Is `anon` a skin buyer?
      1. Yes - you're done.
      2. No - add (**enqueue**) all *their* friends to the **queue**.
  5. Loop back to the top of the **queue**.
  6. If the **queue** is empty, then there are no skin buyers in your network.

  There's a potential problem with this search if two nodes share a connection with each other and we don't deal with duplicates: we could end up with an infinite loop. For example, if I had a Steam friend named `doppelganger` then he and I would be neighbors to each other. That is, when the **queue** gets to `doppelganger`, it will add me to the search **queue**. Then, it will check to see if I will buy one of my own skins and then add my neighbor, `doppelganger`. Therefore, we need to ensure that our search **queue** does not check a node it's already searched. This can be implemented by adding the searched node to a list of searched nodes and refer to it as we work our way down the **queue**.

  The running time for the **BFS** algorithm is `O(V+E)`, such that `V` is the number of *vertices* (nodes) and `E` is the number of *edges* (connections).

* `Shortest-path problem`: a problem in which the objective is to find the shortest, or least, number of discrete units to reach the goal. These kinds of problems are best solved by the **breadth-first search** algorithm.

  For example, finding the least number of bus transfers, least number of moves in chess, shortest walk to the beach, etc.

* `Queue`: an array of items with only two operations, *enqueue* and *dequeue*, such that it follows the method of "[first in, first out](https://en.wikipedia.org/wiki/FIFO_(computing_and_electronics))". It's like a **stack**, except a **queue** is FIFO, and a **stack** is [LIFO](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)).

  * *Enqueue*: add an item to a **queue**.
  * *Dequeue*: delete an item from a **queue**.
