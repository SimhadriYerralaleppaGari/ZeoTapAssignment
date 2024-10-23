# src/ast_node.py
class Node:
    def __init__(self, type, value=None):
        """
        Initialize a new Node.
        :param type: 'operator' for AND/OR, 'operand' for conditions like age > 30.
        :param value: The condition string (e.g., 'age > 30') for operand nodes.
        """
        self.type = type  # 'operator' or 'operand'
        self.value = value  # Stores the condition for operands
        self.left = None  # Left child node (for operators)
        self.right = None  # Right child node (for operators)
