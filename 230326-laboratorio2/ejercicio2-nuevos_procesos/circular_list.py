from typing import TypeVar, Generic
from node import Node

T = TypeVar('T')


class CircularList(Generic[T]):
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def is_empty(self):
        return self.head is None and self.tail is None

    def prepend(self, data: T):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.tail.next = self.head
        self.size += 1

    def append(self, data: T):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node

        self.tail = new_node
        self.tail.next = self.head
        self.size += 1

    def insert_at(self, data: T, i: int):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.size += 1

        else:

            if i == 0:
                self.prepend(data)
            elif i == self.size:
                self.append(data)
            else:
                previous = self.find_at(i - 1)
                new_node.next = previous.next
                previous.next = new_node
                self.size += 1

    def shift(self) -> Node:
        if self.is_empty():
            raise Exception("UnderflowError")

        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current

        else:
            current = self.head
            self.head = current.next
            self.tail.next = None
            current.next = None
            self.tail.next = self.head
            self.size -= 1
            return current

    def pop(self) -> Node:
        if self.is_empty():
            raise Exception('UnderflowError')

        elif self.head is self.tail:
            current = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current

        else:
            current = self.tail
            previous = self.find_at(self.size - 2)
            self.tail = previous
            self.tail.next = None
            previous.next = None
            self.tail.next = self.head
            self.size -= 1
            return current

    def find_by(self, data: T) -> Node:
        current = self.head

        while current is not None:
            if current.data is data:
                return current
            else:
                current = current.next

            if current is self.head:
                break

        raise Exception("Element doesn't exist")

    def find_at(self, i: int):
        current = self.head
        cont = 0

        while current is not None:
            if cont == i:
                return current
            else:
                current = current.next
                cont += 1

            if current is self.head:
                break

        raise Exception("Element doesn't exist")

    def transversal(self) -> str:
        current = self.head
        result = ''

        while current is not self.tail:
            result += str(current.data) + '\n'
            current = current.next

        if not self.is_empty():
            result += str(self.tail.data)

        return result
