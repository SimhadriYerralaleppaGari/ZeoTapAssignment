from ast_node import Node
from rule_parser import create_rule


def combine_rules(rules):
    """
    Combines a list of rule strings into a single AST.
    :param rules: List of rule strings.
    :return: Root node of the combined AST.
    """
    combined_rule = None

    for rule in rules:
        rule_ast = create_rule(rule)

        if combined_rule is None:
            combined_rule = rule_ast
        else:
            # Use 'OR' instead of 'AND' to combine the rules
            new_node = Node(type="operator", value="OR")
            new_node.left = combined_rule
            new_node.right = rule_ast
            combined_rule = new_node

    return combined_rule
