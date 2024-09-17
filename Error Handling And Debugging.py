import traceback

def run_compiler(source_code):
    try:
        lexer = Lexer(source_code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        analyzer = SemanticAnalyzer(ast)
        analyzer.analyze()
        ir_generator = IRGenerator(ast)
        ir = ir_generator.generate()
        optimizer = Optimizer(ir)
        optimized_ir = optimizer.optimize()
        code_generator = CodeGenerator(optimized_ir)
        code = code_generator.generate()
        print("Generated code:", code)
    except Exception as e:
        print("An error occurred:")
        traceback.print_exc()

# Example usage
source_code = "3 + 4 * (2 - 1)"
run_compiler(source_code)
