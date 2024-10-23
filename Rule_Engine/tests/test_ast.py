# tests/test_ast.py
import unittest
from rule_parser import create_rule

class TestAST(unittest.TestCase):
    def test_create_rule(self):
        rule = "age > 30 AND department = 'Sales'"
        ast = create_rule(rule)
        self.assertIsNotNone(ast)  # Ensure AST is created
