"""A simple implementation of a generic stack"""

from typing import Generic, Iterator, TypeVar

_T = TypeVar("_T")


class Node(Generic[_T]):
    """Represent a node in a linked list or stack"""
    def __init__(self, value: _T) -> None:
        self._value = value
        self._next: Node[_T]

    def get_value(self) -> _T:
        """Getter for value"""
        return self._value

    def set_next(self, next_: "Node[_T]") -> None:
        """Setter for next"""
        self._next = next_

    def get_next(self) -> "Node[_T]":
        """Getter for next"""
        return self._next


class StackEmptyError(Exception):
    "Raised when pop/top/peek operation is performed on an empty stack"


class Stack(Generic[_T]):
    """Represent a simple stack using a linked list"""
    def __init__(self) -> None:
        self._head: Node[_T]
        self._size = 0

    def to_string(self, sep: str = " -> ") -> str:
        """
        Get a string representation of the stack using a
        provided separator between element values
        """
        output = ""
        if self._size == 0:
            return output
        current_node = self._head
        for _ in range(self._size - 1):
            output += f"{current_node.get_value()}{sep}"
            current_node = current_node.get_next()
        return f"{output}{current_node.get_value()}"

    def __repr__(self) -> str:
        return self.to_string()

    def __len__(self) -> int:
        return self._size

    def push(self, value: _T) -> None:
        """Push a value to the top of the stack"""
        node = Node(value)
        if self._size > 0:
            node.set_next(self._head)
        self._head = node
        self._size += 1

    def pop(self) -> _T:
        """Pop the topmost value off the stack"""
        if self._size == 0:
            raise StackEmptyError("No value to pop")
        node = self._head
        if self._size > 1:
            self._head = node.get_next()
        else:
            del self._head
        self._size -= 1
        return node.get_value()

    def peek(self) -> _T:
        """Return the value for the topmost item in the stack"""
        if self._size == 0:
            raise StackEmptyError("No value to peek")
        return self._head.get_value()

    def top(self) -> _T:
        """Alias for peek"""
        return self.peek()

    def __iter__(self) -> Iterator[_T]:
        current_node = self._head
        for _ in range(self._size - 1):
            yield current_node.get_value()
            current_node = current_node.get_next()
        yield current_node.get_value()

    def is_empty(self) -> bool:
        """Check if the stack is empty"""
        return self._size == 0
