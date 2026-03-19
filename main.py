import sys
from luz.lexer import Lexer
from luz.parser import Parser
from luz.interpreter import Interpreter

def run(text, interpreter):
    try:
        lexer = Lexer(text)
        tokens = lexer.get_tokens()
        
        parser = Parser(tokens)
        ast = parser.parse()
        
        result = interpreter.visit(ast)
        return result
    except Exception as e:
        error_name = type(e).__name__
        line = getattr(e, 'line', None)
        prefix = f"[Line {line}] " if line is not None else ""
        msg = getattr(e, 'message', str(e))
        print(f"{prefix}{error_name}: {msg}")
        return None

def main():
    interpreter = Interpreter()
    
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                code = f.read()
                run(code, interpreter)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    else:
        print("Luz Interpreter v1.1 - Type 'exit' to terminate")
        while True:
            try:
                text = input("Luz > ")
                if text.strip().lower() == "exit":
                    break
                if not text.strip():
                    continue
                    
                result = run(text, interpreter)
                if result is not None:
                    print(result)
                    
            except KeyboardInterrupt:
                print("\nExiting...")
                break
            except Exception as e:
                error_name = type(e).__name__
                line = getattr(e, 'line', None)
                prefix = f"[Line {line}] " if line is not None else ""
                msg = getattr(e, 'message', str(e))
                print(f"{prefix}{error_name}: {msg}")

if __name__ == "__main__":
    main()
