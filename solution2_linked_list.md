[Return to Linked Lists](2-topic_linked_list.md)
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
```python
# Solution: (there are few that work, this isn't the only one.)
ll = LinkedList()
ll.insert_head(0)
ll.insert_tail(1)
ll.insert_tail(2)
ll.insert_tail(3)
ll.insert_tail(4)
print(ll) #[0, 1, 2, 3, 4]
```
![photo of the first one](img_1.jpg)
#### Problem 2
Keep the same list from the last problem. Remove the number 1, insert a 5 after 2, add 6 after 5, and add 7 at the head. Display the linked list, and draw a picture.
```python
# Solution: (there are few that work, this isn't the only one.)
ll.remove(1)
ll.insert_after(2, 5)
ll.insert_after(5, 6)
ll.insert_head(7)
print(ll) #[7, 0, 2, 5, 6, 3, 4]
```
![photo of the second one](img_2.jpg)
#### Problem 3
Empty the list. Add 8, add 9, put 10 at the head, add 11 after 8, and replace 9 with 12. Display the list, draw a picture.
```python
# Solution: (there are few that work, this isn't the only one.)
#I chose to just reinitialize the list, but you can also call ll.remove_tail() 6 times and ll.remove_head().
ll = LinkedList()
ll.insert_head(8)
ll.insert_tail(9)
ll.insert_head(10)
ll.insert_after(8, 11)
ll.replace(9, 12)
print(ll) #[10, 8, 11, 12]
```
![photo of the third one](img_3.jpg)