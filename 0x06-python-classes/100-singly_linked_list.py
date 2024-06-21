#!/usr/bin/python3

"""This module defines a Node class."""


class Node:
    """
    Class that defines a node of a singly linked list
    """
    def __init__(self, data, next_node=None):
        """
        Initialize a Node.

        Parameters:
        data (int): The data stored in the node.
        next node (Node, optional): The next node in the list.
        Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data of the node.

        Returns:
            int: The data of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the node.

        Args:
            value (int): The new data of the node.

        Raises:
            TypeError: If the data is not an integer..
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node.

        Returns:
            Node: The next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node.

        Args:
            value (Node): The new next node.

        Raises:
            TypeError: If the next node is not a Node
            object or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list.
    """
    def __init__(self):
        """
        Initialize a SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """
        Get a string representation of the List.

        Returns:
            str: A string representation of the list.
        """
        node = self.__head
        result = []
        while node is not None:
            result.append(str(node.data))
            node = node.next_node
        return "\n".join(result)

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted
        positioin in the list.

        Args:
            value (int): The value of the new Node.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and \
                    node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
