class SemanticAnalyzer:
    def __init__(self, ast):
        self.ast = ast
        self.symbol_table = {}

    def analyze(self):
        return self.visit(self.ast)

    def visit(self, node):
        if isinstance(node, tuple):
            if node[0] in ('PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE'):
                left = self.visit(node[1])
                right = self.visit(node[2])
                return left, node[0], right
            elif node[0] == 'NUMBER':
                return float(node[1])
            elif node[0] == 'IDENTIFIER':
                if node[1] not in self.symbol_table:
                    raise RuntimeError(f'Undefined variable {node[1]}')
                return self.symbol_table[node[1]]
        else:
            return node
