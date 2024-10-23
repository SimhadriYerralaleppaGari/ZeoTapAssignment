from ast_node import Node

def create_rule(rule_string):
    """
    Parses a rule string and creates an AST representation.
    """
    tokens = rule_string.split(" ")

    def build_ast(tokens):
        if "AND" in tokens:
            operator_index = tokens.index("AND")
            left_tokens = tokens[:operator_index]
            right_tokens = tokens[operator_index+1:]

            operator_node = Node(type="operator", value="AND")
            operator_node.left = build_ast(left_tokens)
            operator_node.right = build_ast(right_tokens)
            return operator_node

        elif "OR" in tokens:
            operator_index = tokens.index("OR")
            left_tokens = tokens[:operator_index]
            right_tokens = tokens[operator_index+1:]

            operator_node = Node(type="operator", value="OR")
            operator_node.left = build_ast(left_tokens)
            operator_node.right = build_ast(right_tokens)
            return operator_node
        
        else:
            # Convert condition to a valid Python expression
            condition = " ".join(tokens)
            if "=" in condition:
                condition = condition.replace("=", "==")
            return Node(type="operand", value=condition)

    return build_ast(tokens)
