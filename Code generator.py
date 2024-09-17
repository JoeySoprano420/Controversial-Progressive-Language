class CodeGenerator:
    def __init__(self, ir):
        self.ir = ir

    def generate(self):
        # Convert IR to executable code
        return f'print({self.ir})'
