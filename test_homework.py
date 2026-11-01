import unittest

from task1 import find_minimum
from task2 import sum_values
from task3 import min_connection_cost
from tree import BinarySearchTree, Node


class HomeworkTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinarySearchTree.from_values([20, 10, 30, 5, 15, 25, 35])

    def test_find_minimum(self) -> None:
        self.assertEqual(find_minimum(self.tree.root), 5)
        self.assertIsNone(find_minimum(None))

    def test_sum_values(self) -> None:
        self.assertEqual(sum_values(self.tree.root), 140)
        self.assertEqual(sum_values(None), 0)

    def test_cable_connection_cost(self) -> None:
        self.assertEqual(min_connection_cost([8, 4, 6, 12]), 58)
        self.assertEqual(min_connection_cost([10]), 0)
        self.assertEqual(min_connection_cost([]), 0)

    def test_negative_cable_length(self) -> None:
        with self.assertRaises(ValueError):
            min_connection_cost([2, -1])

    def test_tree_with_negative_values(self) -> None:
        root = Node(-3, Node(-8), Node(4))
        self.assertEqual(find_minimum(root), -8)
        self.assertEqual(sum_values(root), -7)


if __name__ == "__main__":
    unittest.main()
