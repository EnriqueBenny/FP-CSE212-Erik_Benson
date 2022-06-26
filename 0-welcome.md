# Python Data Structures Tutorial
---
Welcome to the basic Data Structures tutorial. To fully understand Data Structures, we'll be looking at these topics:

* [Stacks](1-topic_stacks.md)
* [Linked List](2-topic_linked_list.md)
* [Trees](3-topic_trees.md)

For each of the topics, the following format will be used: an intro to the concept, any background needed, an example, and a problem for you to solve.

> Before we begin, it is important to understand what 'Big O' notation is. Big O Notation is an indication of how much memory a set of code will allocate as the dataset grows, it uses these estimates based on the amount of time it will take to fulfill the task. We can break this down in to specific types: O(1), O(n), O($n^{2}$), and O(log n). 
> * O(1) - a consistant time. This will always take the same amount of time, no matter how big the data set gets. An  if/else statement would be an example of this.
> * O(n) - a scaling time. As the dataset increases, the amount of memory needed will also increase linearly. This will be represented in code with a 'for' loop. If there is more than one 'for' loop, write it as O(xn) where x is the number of loops. 
> * O($n^{2}$) - An exponentially increasing time. As the dataset gets bigger, it will take an exponentially greater amount of time for the process to complete. This would be represented in code as a for loop within a for loop.
> * O(log n) - A logarithmic time. Even as the dataset increases the time taken will not increase by too great of an amount - very efficient for massive datasets. This is usually represented in code by taking a dataset and checking if the value you're looking for is in the first or second half, then removing the half that you don't need. Look in the remaning half, determine if it's in the first or second half, and so on, cutting the dataset in half by every searched process. This means that even massive data sets can be handled quite quickly.

## Contact
Questions, comments, concerns:
Erik Benson, BYU-I, CSE 212
Email: erikben@byui.edu