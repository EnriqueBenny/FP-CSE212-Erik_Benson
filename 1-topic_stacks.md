# Stacks
---
[Return to prevous menu](0-welcome.md)
#### Introduction to Stacks
FILO, First In, Last Out. This is the first and most important concept you need to know with a stack. A stack is a linear array of information. It adds values to the end of the array, and removes them from the end of the array, or FILO. It's important to imagine something like a stack of pancakes or of items in a box. You can't just pull from the middle or bottom in either of these scenarios, you have to pull out the stuff on top first, item by item until you reach what you're after.

> In python, the different commands to interact with a stack are as follows:
> * list() - the array used for a stack. 
> * list.append() - adding items on top of the stack - FI (First-In)
> * list.pop() - remove the last item from the list. LO (Last-Out)
#### Example
Copy this code into VS Code:
```python
#create the array
example = list()
#add items to the end of the array (remember FILO)
example.append(0)
example.append(1)
example.append(2)
example.append(3)
example.append(4)
example.append(5)
#remove items from the end of the array (FILO)
example.pop()
example.pop()
example.pop()
print(example)
# Result will be: [0, 1, 2]
example.append(6)
example.append(7)
example.append(8)
example.pop()
example.pop()
example.append(9)
print(example)
# Result will be: [0, 1, 2, 6, 9]
```
#### Problem
Now you try:

```python
#Problem 1
problem = list()
problem.append(0)
problem.append(1)
problem.append(2)
problem.pop()
problem.pop()
problem.append(3)
problem.append(4)
problem.append(5)
problem.append(6)
problem.append(7)
problem.append(8)
problem.pop()
problem.pop()
problem.pop()
problem.append(9)
problem.append(10)
problem.append(11)
problem.append(12)
problem.pop()
problem.append(13)
problem.append(14)
problem.append(15)
problem.append(16)
problem.append(17)
problem.pop()
problem.pop()
problem.append(18)
problem.append(19)
problem.append(20)
#What will the output be? Write it down before you print the list.
#print(problem)

#Problem 2
# We are looking for the output:
# [0, 1, 2, 3, 11, 12, 13, 14, 15, 16]
# Change the variables 'pops' to the proper value to find
# the output we are after.
problem = list()
problem.append(0)
problem.append(1)
problem.append(2)
problem.append(3)
problem.append(4)
problem.append(5)
problem.append(6)
problem.append(7)
problem.append(8)
problem.append(9)
problem.append(10)
#Change pops, will determine how many times the function pop is called. 
pops = 0
for i in range(0, pops):
    problem.pop()
problem.append(11)
problem.append(12)
problem.append(13)
problem.append(14)
problem.append(15)
problem.append(16)
problem.append(17)
problem.append(18)
problem.append(19)
problem.append(20)
#Change pops, will determine how many times the function pop is called. 
pops = 0
for i in range(0, pops):
    problem.pop()
print(problem)
```
Finish the problems, then compare with the solution.
[Solutions](solution1_stacks.py)