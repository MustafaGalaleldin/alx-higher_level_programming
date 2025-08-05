#!/usr/bin/python3
'Singly linked list'


class Node(object):
    'Node in Singly linked list'

    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        if next_node:
            if not isinstance(next_node, Node):
                raise TypeError('next_node must be a Node object')
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if next_node:
            if not isinstance(next_node, Node):
                raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList(object):
    "Singly Linked List"
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new = Node(value, None)
        if not self.head:
            self.head = new
        else:
            go = self.head
            wait = self.head
            while go:
                if go.data < value:
                    if not go.next_node:
                        go.next_node = new
                        break
                    go = go.next_node
                else:
                    if go == wait:
                        new.next_node = go
                        self.head = new
                        break
                    else:
                        while wait.next_node != go:
                            wait = wait.next_node
                        new.next_node = go
                        wait.next_node = new
                        break

    def __str__(self):
        lil = []
        ptr = self.head
        while ptr:
            lil.append(ptr.data)
            ptr = ptr.next_node
        return "\n".join(str(data) for data in lil)
