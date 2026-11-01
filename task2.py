"""Task 2: calculate the sum of all values in a binary search tree."""

from __future__ import annotations

from tree import Node


def sum_values(root: Node | None) -> int:
    """Return the sum of all values in the tree."""
    if root is None:
        return 0

    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        total += node.value
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    return total


if __name__ == "__main__":
    from tree import BinarySearchTree

    tree = BinarySearchTree.from_values([20, 10, 30, 5, 15, 25, 35])
    print(f"Сума значень: {sum_values(tree.root)}")
