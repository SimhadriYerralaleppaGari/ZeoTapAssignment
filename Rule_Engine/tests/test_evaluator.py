# tests/test_evaluator.py
import unittest
from rule_evaluator import evaluate_rule
from rule_combiner import combine_rules

class TestEvaluator(unittest.TestCase):
    def test_evaluate_rule(self):
        rules = ["age > 30", "salary > 50000"]
        combined_ast = combine_rules(rules)
        data = {"age": 35, "salary": 60000}
        result = evaluate_rule(combined_ast, data)
        self.assertTrue(result)
