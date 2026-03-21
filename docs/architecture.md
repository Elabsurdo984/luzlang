# Architecture

Luz follows a classic three-stage interpreter pipeline:

```
Source code (text)
      |
   [Lexer]         luz/lexer.py
      |
 Token stream
      |
   [Parser]        luz/parser.py
      |
  AST (tree)
      |
 [Interpreter]     luz/interpreter.py
      |
   Result
```

## Lexer (`luz/lexer.py`)

Converts raw source text into a flat list of `Token` objects.

- Handles integers, floats (including `.5` notation), strings, format strings, identifiers, keywords, and all operators.
- Tracks line numbers on every token so errors can report the correct source line.
- Resolves string escape sequences (`\n`, `\t`, `\\`, `\"`) at this stage.
- Format strings store the raw template (e.g. `"Hello {name}"`) — expression parsing happens later in the parser.

## Parser (`luz/parser.py`)

Consumes the token stream and builds an **Abstract Syntax Tree (AST)** using a **recursive descent parser**.

Operator precedence is enforced through a chain of parsing functions, each calling the next higher-precedence level:

```
logical_or → logical_and → logical_not → comparison
           → arithmetic → term → power → factor
```

Each node type (`BinOpNode`, `IfNode`, `CallNode`, `ClassDefNode`, etc.) is a plain Python class defined at the top of the file. Nodes hold references to their child nodes, forming a tree.

Format string parsing: the lexer stores raw template text; the parser splits it on `{...}` (tracking brace depth for nesting), then sub-parses each embedded expression using a fresh `Lexer` + `Parser`.

## Interpreter (`luz/interpreter.py`)

Walks the AST using the **Visitor pattern**: `visit(node)` dispatches to `visit_IfNode`, `visit_BinOpNode`, etc. based on the node's class name.

**Scope** is managed through a chain of `Environment` objects. Each block or function call creates a new environment linked to its parent, enabling proper variable scoping and closures.

**OOP** is implemented through:

| Object | Role |
|---|---|
| `LuzClass` | Stores the method dictionary and a reference to the parent class |
| `LuzInstance` | Stores the instance's attribute dictionary and a reference to its class |
| `LuzSuperProxy` | Wraps an instance + a parent class; resolves `super.method()` calls |
| `LuzFunction` | A named function with a closure |
| `LuzLambda` | An anonymous function (short `fn(x) => expr` or long `fn(x) { body }`) |

Method calls automatically inject `self` and `super` into the method's local scope.

**Control flow signals** (`return`, `break`, `continue`) are implemented as Python exceptions that propagate up the call stack and are caught at the appropriate node handler.

## Error system (`luz/exceptions.py`)

All errors inherit from `LuzError`:

```
LuzError
├── SyntaxFault       (lexer / parser errors)
├── SemanticFault     (type errors, undefined variables, wrong argument count…)
│   ├── AttributeNotFoundFault
│   └── ArityFault
├── RuntimeFault      (division by zero, index out of bounds…)
├── CastFault         (failed type conversion)
└── UserFault         (raised by the alert keyword)
```

Every error carries a `line` attribute that is attached when the error propagates through `visit()`.

## File overview

```
luz-lang/
├── main.py               # Entry point: REPL and file execution
├── luz/
│   ├── tokens.py         # TokenType enum and Token class
│   ├── lexer.py          # Lexer: text → tokens
│   ├── parser.py         # Parser: tokens → AST + all AST node classes
│   ├── interpreter.py    # Interpreter: executes the AST
│   └── exceptions.py     # Full error class hierarchy
├── tests/
│   └── test_suite.py     # Test suite
├── docs/                 # This documentation (MkDocs)
├── vscode-luz/           # VS Code syntax highlighting extension
└── examples/             # Example programs
```
