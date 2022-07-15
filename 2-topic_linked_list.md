# Linked Lists
---
[Previous Topic](1-topic_stacks.md)

[Main menu](0-welcome.md)

[Next topic](3-topic_trees.md)
#### Intro
A linked list is an array of information that is not adjacent to each other. Each value in a linked list contains both values and pointers that guide the program from one value to another.

#### Pointers
Pointers are a concept in programming where a value will contain information that indicates where to find related information. You can think of it like piece of string that stretches from one point to another. Pointers are a very important concept, as when a program passes a value by reference, it always uses a pointer to indicate the original value. In this case, pointers point to the next item in the linked list, and the previous item.

#### Adding/Removing from a Linked List
With an understanding of what a linked list is, and what pointers are, it's not hard to understand why pointers are the most important aspect of a linked list. If the pointers don't work, then it's impossible to find the next piece of information in the linked list, and your link is broken.
When adding an item to a linked list, a pointer to the previous item, and a pointer from the previous item to the current one both need to be set. This is done using the Node class (see below), with Node.next being your pointer to the next item, and Node.prev being your pointer to the previous item. These pointers will always need to be reassigned whenever you make changes to a value on the list. 
If you are removing from the list, then the pointers that went to the value you're removing need to be reassigned to point at the values before and after it in the linked list.
The first item in the linked list will NOT have a pointer to a previous item, as there is none, and the last item will not have a next pointer.

#### Example of a linked list class
```python
class LinkedList:
    """
    Our linkedlist class, it containes the class Node, which will represent each item on our linked list.
    """

    class Node:
        """
        The node contains the values for each point in the linked list, as well as the pointers to the previous and next values.
        """

        def __init__(self, data):
            """ 
            Initialize the node. Pointers will have to be changed after every value is added.
            """
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        """
        Initialize an empty linked list.
        head is the beginning of the list.
        tail is the end of the list.
        """
        self.head = None
        self.tail = None

    def insert_head(self, value):
        """
        Insert a new node at the front (i.e. the head) of the
        linked list.
        """
        # Create the new node
        new_node = LinkedList.Node(value)  
        
        # If the list is empty, then point both head and tail
        # to the new node.
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # If the list is not empty, then only self.head will be
        # affected.
        else:
            new_node.next = self.head  # Connect new node to the previous head     
            self.head.prev = new_node  # Connect the previous head to the new node 
            self.head = new_node       # Update the head to point to the new node   

    def insert_tail(self, value):
        """
        Insert a new node at the back (i.e. the tail) of the 
        linked list.
        """
        new_node = LinkedList.Node(value)
        if self.tail is None and self.head is None:
            self.head = new_node
            self.tail = new_node
        elif self.tail is None:
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_head(self):
        """ 
        Remove the first node (i.e. the head) of the linked list.
        """
        # If the list has only one item in it, then set head and tail 
        # to None resulting in an empty list.  This condition will also
        # cover an empty list.  Its okay to set to None again.
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # If the list has more than one item in it, then only self.head
        # will be affected.
        elif self.head is not None:
            self.head.next.prev = None  # Disconnect the second node from the first node
            self.head = self.head.next  # Update the head to point to the second node

    def remove_tail(self):
        """
        Remove the last node (i.e. the tail) of the linked list.
        """
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev


    def insert_after(self, value, new_value):
        """
        Insert 'new_value' after the first occurance of 'value' in
        the linked list.
        """
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        current = self.head
        while current is not None:
            if current.data == value:
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                if current == self.tail:
                    self.insert_tail(new_value)
                # For any other location of 'value', need to create a 
                # new node and reconenct the links to insert.
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = current       # Connect new node to the node containing 'value'
                    new_node.next = current.next  # Connect new node to the node after 'value'
                    current.next.prev = new_node  # Connect node after 'value' to the new node
                    current.next = new_node       # Connect the node containing 'value' to the new node
                return # We can exit the function after we insert
            current = current.next # Go to the next node to search for 'value'

    def remove(self, value):
        """
        Remove the first node that contains 'value'.
        """
        # Search for the node that matches 'value' by starting at the 
        # head of the list.
        current = self.head
        while current is not None:
            if current.data == value:
                if current is self.head:
                    self.remove_head()
                elif current is self.tail:
                    self.remove_tail()
                # If the location of 'value' is at the end of the list,
                # then we can call insert_tail to add 'new_value'
                else:
                    current.next.prev = current.prev
                    current.prev.next = current.next
                    current = None
                    
                return # We can exit the function after we remove
            current = current.next

    def replace(self, old_value, new_value):
        """
        Searrch for all instances of 'old_value' and replace the value 
        to 'new_value'.
        """
        current = self.head
        while current is not None:
            if current.data == old_value:
                current.data = new_value
            current = current.next # Go to the next node to search for 'value'

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        current = self.head  # Start at the begining since this is a forward iteration.
        while current is not None:
            yield current.data  # Provide (yield) each item to the user
            current = current.next # Go forward in the linked list

    def __reversed__(self):
        """
        Iterate backward through the Linked List
        """
        current = self.tail
        while current is not None:
            yield current.data 
            current = current.prev

    def __str__(self):
        """
        Return a string representation of the linked list.
        """
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output
```

#### Problem 1
Add items to the linked list above by calling the class and the methods within it. Add five numbers, from 0 to 4, then display items in the linked list. Draw a picture to go along with it.

#### Problem 2
Keep the same list from the last problem. Remove the number 1, insert a 5 after 2, add 6 after 5, and add 7 at the head. Display the linked list, and draw a picture.

#### Problem 3
Empty the list. Add 8, add 9, put 10 at the head, add 11 after 8, and replace 9 with 12. Display the list, draw a picture.

[Solutions](solution2_linked_list.md)