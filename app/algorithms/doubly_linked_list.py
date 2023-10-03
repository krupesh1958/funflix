# !/usr/bin/env python3
"""Implement Doubly Linked List"""
from __future__ import annotations

from typing import DefaultDict, Any


class LinkedNode:
    """
    Linked node implement for doubly linked list
    Linked node constrains three instace variables
    ```LinkedNode(prev, data, next)```
    """
    def __init__(self, data):
        self.prev: LinkedNode[DefaultDict] = None
        self.data: int | Any = data
        self.next: LinkedNode[DefaultDict] = None


    def __str__(self):
        return f"{self.data}"


class DoublyLinkedList:
    """Implement doubly linked list as efficient way"""

    
    def __init__(self):
        self.head: LinkedNode[DefaultDict] = None
        self.tail: LinkedNode[DefaultDict] = None


    def __iter__(self):
        """
        >>> dll = DoublyLinkedList()
        >>> dll.insert_at_head('A')
        >>> dll.insert_at_tail('B')
        >>> tuple(dll) | list(dll)
        ('A', 'B') | list(dll)
        """
        node = self.head
        while node:
            yield node.data
            node = node.next


    def __str__(self):
        """
        >>> dll = DoublyLinkedList()
        >>> dll.insert_at_head('A')
        >>> dll.insert_at_tail('B')
        >>> dll
        A -> B
        """
        return '->'.join([str(itr) for itr in self])


    def __len__(self):
        """
        >>> dll = DoublyLinkedList()
        >>> dll.insert_at_head('A')
        >>> dll.insert_at_tail('B')
        >>> len(dll)
        2
        """
        return sum(1 for _ in self)


    def insert_at_head(self, data):
        """
        >>> dll = DoublyLikedList()
        >>> dll.insert_at_head('A')
        >>> dll.insert_at_tail('B')
        A - B
        """
        self.insert_at_nth(0, data)
        return


    def insert_at_tail(self, data):
        """
        >>> dll = DoublyLikedList()
        >>> dll.insert_at_head('A')
        >>> dll.insert_at_tail('B')
        >>> dll.insert_at_tail('C')
        A - B - C
        """
        self.insert_at_nth(len(self), data)
        return


    def insert_at_nth(self, index: int, data: Any):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.insert_at_nth(-1, 666)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> linked_list.insert_at_nth(1, 666)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> linked_list.insert_at_nth(0, 2)
        >>> linked_list.insert_at_nth(0, 1)
        >>> linked_list.insert_at_nth(2, 4)
        >>> linked_list.insert_at_nth(2, 3)
        >>> str(linked_list)
        '1->2->3->4'
        >>> linked_list.insert_at_nth(5, 5)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        """
        length = len(self)
        assert 0 <= index <= length, "Index out of range"

        node = LinkedNode(data)
        if not self.head:
            self.head = self.tail = node
        
        # Head insertion
        elif index == 0:
            self.head.prev = node
            node.next = self.head
            self.head = node

        # Tail insertion
        elif length == index:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        # Nth position insertion
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.prev.next = node
            node.prev = temp.prev
            node.next = temp
            temp.prev = node
        return


    def is_empty(self):
        """
        Checking linked list is empty

        :rtype: bool
        """
        return len(self) == 0


    def delete_at_head(self):
        """
        >>> dll = DoublyLikedList()
        >>> dll.insert_at_head('A')
        >>> dll.insert_at_tail('B')
        >>> dll.insert_at_tail('C')
        A - B - C
        >>> dll.delete_at_head()
        B - C
        """
        self.delete_at_nth(0)


    def delete_at_tail(self):
        """
        >>> dll = DoublyLikedList()
        >>> dll.insert_at_head('A')
        >>> dll.insert_at_tail('B')
        >>> dll.insert_at_tail('C')
        A - B - C
        >>> dll.delete_at_tail()
        A - B
        """
        self.delete_at_nth(len(self))


    def delete_at_nth(self, index: int):
        """
        >>> linked_list = DoublyLinkedList()
        >>> linked_list.delete_at_nth(-1, 666)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> linked_list.delete_at_nth(1, 666)
        Traceback (most recent call last):
            ....
        IndexError: list index out of range
        >>> linked_list.insert_at_nth(0, 2)
        >>> linked_list.insert_at_nth(0, 1)
        >>> linked_list.insert_at_nth(2, 4)
        >>> linked_list.insert_at_nth(2, 3)
        >>> str(linked_list)
        '1->2->3->4'
        >>> linked_list.delete_at_nth(2)
        '1->2->4'
        """
        length = len(self)
        assert 0 <= index <= length, "Index out of range"

        if index == 1:
            self.head = self.tail = None

        # Remove at head
        elif index == 0:
            self.head = self.head.next
            self.head.prev = None

        # Remove at tail
        elif index == length:
            self.tail = self.tail.prev            
            self.tail.next = None

        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
        return


    def prev_node(self, data):
        return self.prev_next_node(prev=True, data=data)


    def next_node(self, data):
        return self.prev_next_node(next=True, data=data)


    def prev_next_node(self, data, prev=False, next=False):
        """
        >>> dll = DoublyLinkedList
        >>> dll.insert_at_head('A')
        >>> dll.insert_at_tail('B')
        >>> dll.insert_at_tail('C')
        A - B - C
        >>> dll.prev_node('B')
        A
        >>> dll.next_node('A')
        B
        """
        # If data match to self.head
        if self.head.data == data:
            return self.head.next.data if next else None

        # If data match to self.tail
        elif self.tail.data == data:
            return self.tail.prev.data if prev else None

        # Need to found
        while self.head and self.head.data != data:
            self.head = self.head.next

        # If data not found
        if not self.head:
            return 0

        return self.head.prev.data if prev else self.head.next.data
