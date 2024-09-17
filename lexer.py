import re
from typing import List, Tuple

class Lexer:
    def __init__(self, source_code: str):
        self.source_code = source_code
        self.tokens = []
        self.token_specification = [
            ('NUMBER',    r'\d+(\.\d*)?'),
            ('IDENTIFIER',r'[A-Za-z_][A-Za-z_0-9]*'),
            ('ASSIGN',    r'='),
            ('PLUS',      r'\+'),
            ('MINUS',     r'-'),
            ('MULTIPLY',  r'\*'),
            ('DIVIDE',    r'/'),
            ('LPAREN',    r'\('),
            ('RPAREN',    r'\)'),
            ('SKIP',      r'[ \t]+'),
            ('MISMATCH',  r'.'),
        ]
        self.regex_patterns = '|'.join(f'(?P<{pair[0]}>{pair[1]})' for pair in self.token_specification)
        self.regex = re.compile(self.regex_patterns)

    def tokenize(self) -> List[Tuple[str, str]]:
        for match in self.regex.finditer(self.source_code):
            for token_type, token_value in match.groupdict().items():
                if token_value:
                    if token_type == 'SKIP':
                        continue
                    if token_type == 'MISMATCH':
                        raise RuntimeError(f'Unexpected character: {token_value}')
                    self.tokens.append((token_type, token_value))
        return self.tokens
