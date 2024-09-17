class IRGenerator:
    def __init__(self, ast):
        self.ast = ast

    def generate(self):
        return self.visit(self.ast)

    def visit(self, node):
        if isinstance(node, tuple):
            if node[0] in ('PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE'):
                left = self.visit(node[1])
                right = self.visit(node[2])
                return f'({left} {node[0]} {right})'
            elif node[0] == 'NUMBER':
                return node[1]
            elif node[0] == 'IDENTIFIER':
                return node[1]
        else:
            return node
