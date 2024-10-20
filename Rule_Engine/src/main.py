# src/main.py
from rule_parser import create_rule
from rule_combiner import combine_rules
from rule_evaluator import evaluate_rule

if __name__ == "__main__":
    # Example rule strings
    rule1 = "age > 30 AND department = 'Sales'"
    rule2 = "age < 25 AND department = 'Marketing'"

    # Parse the rules
    rule1_ast = create_rule(rule1)
    rule2_ast = create_rule(rule2)

    # Combine the rules
    combined_ast = combine_rules([rule1, rule2])

    # Example user data
    user_data = {
        "age": 35,
        "department": "Sales",
        "salary": 60000
    }

    # Evaluate the combined rule against user data
    result = evaluate_rule(combined_ast, user_data)
    print(f"Evaluation Result: {result}")  # True or False
