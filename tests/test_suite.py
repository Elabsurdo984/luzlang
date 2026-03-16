import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from luz.lexer import Lexer
from luz.parser import Parser
from luz.interpreter import Interpreter

def test_arithmetic():
    print("Probando aritmética...")
    interpreter = Interpreter()
    cases = [("1 + 2 * 3", 7.0), ("(1 + 2) * 3", 9.0), ("10 / 2 - 1", 4.0)]
    for code, expected in cases:
        tokens = Lexer(code).get_tokens()
        ast = Parser(tokens).parse()
        assert interpreter.visit(ast) == expected
    print("Aritmética: OK")

def test_variables_and_strings():
    print("Probando variables y strings...")
    interpreter = Interpreter()
    # Variables y concatenación
    code = 'a = "hola" b = " mundo" res = a + b'
    interpreter.visit(Parser(Lexer(code).get_tokens()).parse())
    assert interpreter.symbol_table['res'] == "hola mundo"
    
    # Multiplicación de strings
    code = 'risa = "ja" * 3'
    interpreter.visit(Parser(Lexer(code).get_tokens()).parse())
    assert interpreter.symbol_table['risa'] == "jajaja"
    print("Variables y strings: OK")

def test_control_flow():
    print("Probando flujo de control (if, while, for)...")
    interpreter = Interpreter()
    
    # If/Else
    code = 'x = 10 if x > 5 { res = "si" } else { res = "no" }'
    interpreter.visit(Parser(Lexer(code).get_tokens()).parse())
    assert interpreter.symbol_table['res'] == "si"
    
    # While
    code = 'i = 0 while i < 5 { i = i + 1 }'
    interpreter.visit(Parser(Lexer(code).get_tokens()).parse())
    assert interpreter.symbol_table['i'] == 5.0
    
    # For
    code = 'total = 0 for k = 1 to 5 { total = total + k }'
    interpreter.visit(Parser(Lexer(code).get_tokens()).parse())
    assert interpreter.symbol_table['total'] == 15.0
    print("Flujo de control: OK")

def test_logical_and_booleans():
    print("Probando booleanos y lógica...")
    interpreter = Interpreter()
    cases = [
        ("true and false", False),
        ("true or false", True),
        ("not false", True),
        ("10 > 5 and not (2 == 3)", True)
    ]
    for code, expected in cases:
        tokens = Lexer(code).get_tokens()
        ast = Parser(tokens).parse()
        assert interpreter.visit(ast) == expected
    print("Booleanos y lógica: OK")

def test_functions():
    print("Probando funciones...")
    interpreter = Interpreter()
    code = '''
    function factorial(n) {
        if n <= 1 { return 1 }
        return n * factorial(n - 1)
    }
    res = factorial(5)
    '''
    interpreter.visit(Parser(Lexer(code).get_tokens()).parse())
    assert interpreter.symbol_table['res'] == 120.0
    print("Funciones y recursividad: OK")

def run_all():
    print("=== INICIANDO SUITE DE PRUEBAS DE LUZ ===\n")
    try:
        test_arithmetic()
        test_variables_and_strings()
        test_control_flow()
        test_logical_and_booleans()
        test_functions()
        print("\n=== ¡TODAS LAS PRUEBAS PASARON CON ÉXITO! ===")
    except Exception as e:
        print(f"\nERROR EN LAS PRUEBAS: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_all()
