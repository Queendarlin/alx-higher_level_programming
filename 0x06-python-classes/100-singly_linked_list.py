#!/usr/bin/python3
"""Python file to define Node class"""


class Node:
    """Node class for a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes a new Node instance with data and next_node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the value of data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the value of data with type validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the value of next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the value of next_node with type validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """SinglyLinkedList class for a singly linked list"""

    def __init__(self):
        """Initializes a new SinglyLinkedList instance with head set to None"""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list"""
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            cur = self.head
            while cur.next_node is not None and cur.next_node.data < value:
                cur = cur.next_node

            new_node.next_node = cur.next_node
            cur.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list"""
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
