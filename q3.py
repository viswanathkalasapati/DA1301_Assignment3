from typing import Optional


class TreeNode:
    """Binary tree node for the org chart."""
    def __init__(self, salary=0, left=None, right=None):
        self.salary = salary
        self.left = left
        self.right = right


def count_fair_managers(root: Optional[TreeNode]) -> int:
    """
    Problem 3: Fair managers in an org chart.

    Given the root of a binary tree where each node has a `salary`,
    count the number of nodes whose salary equals the floor-division
    average salary of their entire subtree (including themselves).

    Args:
        root: root TreeNode of the org chart (or None for empty chart).

    Returns:
        Number of fair managers in the tree.
    """
    count = 0

    def dfs(node):
        nonlocal count
        if not node:
            return 0, 0

        left_sum, left_count = dfs(node.left)
        right_sum, right_count = dfs(node.right)

        total_sum = left_sum + right_sum + node.salary
        total_count = left_count + right_count + 1

        if node.salary == total_sum // total_count:
            count += 1

        return total_sum, total_count

    dfs(root)
    return count


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    # root = [1] -> a single employee is trivially a fair manager
    root = TreeNode(1)
    print(count_fair_managers(root))  # expected: 1
