import ast
from Node import Node


class LogicParser():
    def __init__(self, logic):
        self.logicstring = logic
        self.asttree = ast.parse(logic).body[0].value
        self.tree = self.to_tree(self.asttree)

    def to_tree(self, tree):
        if isinstance(tree, ast.BoolOp):
            if isinstance(tree.op, ast.And):
                name = "and"
            else:
                name = "or"
            return Node(name, self.to_tree(tree.values[0]), self.to_tree(tree.values[1]))
        elif isinstance(tree, ast.UnaryOp):
            if isinstance(tree.operand, ast.BoolOp):
                if isinstance(tree.operand.op, ast.And):
                    name = "and"
                else:
                    name = "or"
                return Node("not", None,
                            Node(name, self.to_tree(tree.operand.values[0]), self.to_tree(tree.operand.values[1])))
            else:
                return Node("not", None, Node(tree.operand.id))
        else:
            return Node(tree.id)
