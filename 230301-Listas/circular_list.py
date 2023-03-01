from node import Node
from typing import TypeVar, Generic

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
        # La lista esta vacia (mover head y tail)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head
            self.head = new_node
            # Hasta este punto esta en lazada

        self.tail.next = self.head
        self.size += 1
        # La lista tiene al menos un elemento (mover)

    def transversal(self) -> str:
        # head = None
        # tali = None
        # current = None
        current = self.head
        result = ''
        while current is not self.tail:
            result += str(current.data) + '->'
            current = current.next

        if current is not None:
            result += str(current.data)

        return result








