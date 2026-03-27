# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Run all tests
python -m pytest tests/test_suite.py -v

# Run a specific test class or test
python -m pytest tests/test_suite.py::TestArithmetic -v
python -m pytest tests/test_suite.py::TestArithmetic::test_int_addition -v

# Run the interpreter (REPL)
python main.py

# Run a .luz file
python main.py file.luz

# Parse-only check (used by VS Code extension)
python main.py --check file.luz

# Lint
pylint luz/

# Build the C lexer (Windows — requires MSYS2)
cd luz/c_lexer && make
```

## Architecture

The interpreter is a classic three-stage pipeline: **Lexer → Parser → Interpreter**.

The entry point for all execution is `run(text, interpreter)` in `main.py`, which chains these three stages. The `Interpreter` object is stateful and persists the global environment across calls (used by the REPL).

### Lexer (`luz/lexer.py`)

Converts source text to a flat `list[Token]`. The `get_tokens()` method is the single entry point. If `luz/c_lexer/luz_lexer.dll` (Windows) or `.so` (Linux/Mac) is present, it transparently delegates to the C implementation via `luz/c_lexer/bridge.py`. Otherwise it falls back to pure Python. The `_USE_C_LEXER` module-level flag controls this.

### Parser (`luz/parser.py`)

Recursive-descent parser that converts `list[Token]` to a list of AST nodes. Each grammar rule is a method; operator precedence is encoded as a call chain (`logical_or → logical_and → comparison → addition → multiplication → unary → atom`). AST node classes are plain data containers — all logic lives in the interpreter.

### Interpreter (`luz/interpreter.py`)

Tree-walking evaluator using the visitor pattern: `visit(node)` dispatches to `visit_<ClassName>(node)`. The key runtime objects are:

- **`Environment`** — lexical scope chain with `define/lookup/assign`. `is_function_scope=True` prevents assignment from leaking through closures.
- **`LuzFunction`** — wraps a `FuncDefNode` + closure `Environment`. Supports default params, variadic (`...args`), and named kwargs.
- **`LuzLambda`** — anonymous functions (`fn(x) => expr` or `fn(x) { body }`).
- **`LuzClass` / `LuzInstance` / `BoundMethod`** — class system. Methods in Luz take `self` as an **explicit** first parameter — it is never implicit.
- **`LuzModule`** — wraps a module's exported namespace for `import "x" as alias`.

Control flow (`return`, `break`, `continue`) is implemented via Python exceptions (`ReturnException`, `BreakException`, `ContinueException`). These are caught at the appropriate scope, not by user-level `attempt/rescue`.

### Errors (`luz/exceptions.py`)

All errors are subclasses of `LuzError` which carries `.line`, `.col`, and `.message`. The hierarchy splits into `SyntaxFault` (parse-time), `SemanticFault` (runtime logic), `RuntimeFault` (execution), and `UserFault` (raised by `alert`). Control flow exceptions (`ReturnException` etc.) also extend `LuzError` but are not real errors.

## Important Patterns

**Class methods require explicit `self`:** Unlike Python, Luz class methods must declare `self` as the first parameter. The interpreter prepends the instance to the argument list when calling methods.

```luz
class Foo {
    function init(self, x) { self.x = x }
    function get(self) { return self.x }
}
```

**Method names must not shadow builtins:** If a class method is named `len`, `min`, `max`, or `sum`, it will shadow the builtin inside the class body, causing `ArityFault` when the interpreter tries to call the builtin with the wrong number of args. Use alternative names (`size`, `minimum`, `maximum`, `total`).

**Import resolution order:** `import "math"` resolves by trying in order: literal path → `luz_modules/math/` → file-relative path → `$LUZ_HOME/lib/` → `libs/luz-math/math.luz` (dev fallback). Circular imports are silently skipped via `self.imported_files` (set of absolute paths).

**`from "x" import ...` and `import "x" as ...`** execute the module in an isolated `Environment`. Plain `import "x"` executes in the current scope.

## Standard Library (`libs/`)

Each library lives in `libs/luz-<name>/` with an entry-point `<name>.luz` that imports submodules. Users write `import "math"` which resolves to `libs/luz-math/math.luz`.

Trig and log functions (`sin`, `cos`, `exp`, `ln`, etc.) are implemented as **native Python builtins** in `interpreter.py`, not as Luz code. The `libs/luz-math/trigonometry.luz` and `logarithms.luz` files are thin wrappers that only add utility functions on top.

## C Lexer (`luz/c_lexer/`)

- `luz_lexer.c` — C implementation of the full lexer
- `bridge.py` — ctypes bridge; `_C_TO_PYTHON` list maps C enum indices to Python `TokenType`
- `Makefile` — uses MSYS2's `bash` + `gcc` on Windows (requires MSYS2 at `C:/msys64`)
- The `.dll`/`.so` is gitignored; run `make` to build it locally
- `INT` and `FLOAT` token values must be converted from string to `int`/`float` in the bridge
