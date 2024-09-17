from typing import List, Tuple

class Parser:
    def __init__(self, tokens: List[Tuple[str, str]]):
        self.tokens = tokens
        self.current_token = None
        self.position = 0

    def get_next_token(self):
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
            self.position += 1
        else:
            self.current_token = ('EOF', '')

    def parse(self):
        self.get_next_token()
        return self.expr()

    def expr(self):
        result = self.term()
        while self.current_token[0] in ('PLUS', 'MINUS'):
            op = self.current_token
            self.get_next_token()
            result = (op, result, self.term())
        return result

    def term(self):
        result = self.factor()
        while self.current_token[0] in ('MULTIPLY', 'DIVIDE'):
            op = self.current_token
            self.get_next_token()
            result = (op, result, self.factor())
        return result

    def factor(self):
        token_type, token_value = self.current_token
        if token_type == 'NUMBER':
            self.get_next_token()
            return ('NUMBER', token_value)
        elif token_type == 'IDENTIFIER':
            self.get_next_token()
            return ('IDENTIFIER', token_value)
        elif token_type == 'LPAREN':
            self.get_next_token()
            result = self.expr()
            if self.current_token[0] != 'RPAREN':
                raise RuntimeError('Expected closing parenthesis')
            self.get_next_token()
            return result
        else:
            raise RuntimeError('Unexpected token')
