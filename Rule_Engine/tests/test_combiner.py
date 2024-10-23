# tests/test_combiner.py
import unittest
from rule_combiner import combine_rules

class TestCombiner(unittest.TestCase):
    def test_combine_rules(self):
        rules = ["age > 30", "salary > 50000"]
        combined_ast = combine_rules(rules)
        self.assertIsNotNone(combined_ast)  # Ensure AST is combined
