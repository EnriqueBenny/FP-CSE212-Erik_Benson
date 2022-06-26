# Stacks
---
[Return to prevous menu](0-welcome.md)
#### Introduction to Stacks
FILO, First In, Last Out. This is the first and most important concept you need to know with a stack. A stack is a linear array of information. It adds values to the end of the array, and removes them from the end of the array, or FILO. It's important to imagine something like a stack of pancakes or of items in a box. You can't just pull from the middle or bottom in either of these scenarios, you have to pull out the stuff on top first, item by item until you reach what you're after.

> In python, the different commands to interact with a stack are as follows:
> * list() - the array used for a stack. 
> * list.append() - adding items on top of the stack - FI (First-In)
> * list.pop() - remove the last item from the list. LO (Last-Out)

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
```