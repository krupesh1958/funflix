# !/usr/bin/env python3
"""Implement Doubly Linked List"""
from __future__ import annotations

from typing import Any, DefaultDict


class LinkedNode:
    """
    Linked node implement for doubly linked list
    Linked node constrains three instace variables
    ```LinkedNode(prev, data, next)```
    """
    def __init__(self, prev, data, next):
        self.prev: LinkedNode[DefaultDict] = None
        self.data: int = None
        self.nextL: LinkedNode[DefaultDict] = None


class DoublyLinkedList:
    """Impliment doubly linked list"""
    head: LinkedNode[DefaultDict] = None


    def insert_front(self, data):
        """
        Insert at front
        i.e. LinkedNode[1, 2 -> 1, 3 -> 2 -> 1]

        :type data: int
        :rtype: None
        """
        if not self.head:
            self.head = LinkedNode(data)
        else:
            temp = LinkedNode(data)
            self.head.prev = temp
            temp.next = self.head
            self.head = temp
        return

    def __delattr__(self, data):
        """
        Delete node on doubly linked list

        :type value: int
        
        """