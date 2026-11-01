"""Task 1: find the smallest value in a binary search tree."""

from __future__ import annotations

from tree import Node


def find_minimum(root: Node | None) -> int | None:
    """Return the smallest value in the tree, or None for an empty tree."""
    if root is None:
        return None

    current = root
    while current.left is not None:
        current = current.left
    return current.value


if __name__ == "__main__":
    from tree import BinarySearchTree

    tree = BinarySearchTree.from_values([20, 10, 30, 5, 15, 25, 35])
    print(f"Найменше значення: {find_minimum(tree.root)}")
