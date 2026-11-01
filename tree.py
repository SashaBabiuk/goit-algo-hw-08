"""Binary search tree used by tasks 1 and 2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None


class BinarySearchTree:
    """A binary search tree that ignores duplicate values."""

    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value == current.value:
                return
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    return
                current = current.right

    @classmethod
    def from_values(cls, values: list[int]) -> "BinarySearchTree":
        tree = cls()
        for value in values:
            tree.insert(value)
        return tree
