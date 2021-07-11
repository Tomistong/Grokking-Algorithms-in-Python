# Recursion

## Chapter terms

* [`Recursion`](https://en.wikipedia.org/wiki/Recursion_(computer_science)): a method of solving a problem where the solution depends on solutions to smaller instances of the same problem. More simply, it's when a function calls itself.

Additionally, **recursion** is when the output of a thing is used as input to call the same thing, again. For example, when a function calls itself depending on the evaluation of a condition. You should use **recursion** when it makes a problem more clear to grok.

However, it's easy to write a runaway **recursive** function that calls itself infinitely. For example, a function that counts down from some integer would most likely use **recursion** to solve this problem and be at risk of never finishing if no conditions are added to provide the function a way of exiting. ***YOU NEED TO TELL A RECURSIVE FUNCTION WHEN TO STOP***. Therefore, every recursive function has two parts: the *base case* and the *recursive case*.

* `Base case`: the condition that *exits* recursion.

* `Recursive case`: the condition that *continues* recursion.

* [`Stack`](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)): a collection of items that only has two actions: *push* (insert) and *pop* (remove and read). The order in which items are added/removed uses a method of managing items called [LIFO](https://en.wikipedia.org/wiki/FIFO_and_LIFO_accounting#LIFO) (last in first out).

* [`Call stack`](https://en.wikipedia.org/wiki/Call_stack): the internal **stack** used by your computer.

The call stack is useful especially in the case of recursion. It helps keep track of things partially evaluated even when it's `n` recusions deep and finds a dead end. That is, when it resolves the "dead end" it will work it's way backwards from the top of the *call stack*. However, the drawback is that having a tall *stack* needs a lot of memory. Too many recursive function calls will ultimately lead you to one of two options:

* Rewrite your code to operate on a `for loop`, or
* Use something called *tail recursion*.
