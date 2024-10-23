# src/rule_evaluator.py
def evaluate_rule(node, data):
    """
    Evaluates the rule represented by the AST against the provided user data.
    :param node: Root of the AST to evaluate.
    :param data: User data to check (e.g., {"age": 35, "salary": 60000}).
    :return: True if the user satisfies the rule, False otherwise.
    """
    if node.type == "operand":
        # Evaluate condition against user data
        # Example: node.value is 'age > 30' -> evaluate as data['age'] > 30
        return eval(node.value, {}, data)  # Careful with eval, sanitize input in production

    elif node.type == "operator":
        # Recursively evaluate the left and right children
        left_result = evaluate_rule(node.left, data)
        right_result = evaluate_rule(node.right, data)

        if node.value == "AND":
            return left_result and right_result
        elif node.value == "OR":
            return left_result or right_result

    return False
