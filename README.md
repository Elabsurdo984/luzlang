# Luz Programming Language

**Luz** is a lightweight, interpreted programming language written in Python. It is designed to be simple, readable, and easy to learn — making it a great starting point for understanding how programming languages work under the hood.

```
name = listen("What is your name? ")
write("Hello, " + name + "!")

for i = 1 to 5 {
    if i % 2 == 0 {
        write(i, "is even")
    } else {
        write(i, "is odd")
    }
}
```

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Language Reference](#language-reference)
  - [Types](#types)
  - [Variables](#variables)
  - [Operators](#operators)
  - [Control Flow](#control-flow)
  - [Functions](#functions)
  - [Error Handling](#error-handling)
  - [Modules](#modules)
  - [Built-in Functions](#built-in-functions)
- [Architecture](#architecture)
- [Running Tests](#running-tests)

---

## Features

- **Dynamic typing** — integers, floats, strings, booleans, lists, dictionaries
- **Arithmetic operators** — `+`, `-`, `*`, `/`, `%`, `**`
- **String operations** — indexing, escape sequences, and 11 built-in string functions
- **Control flow** — `if / elif / else`, `while`, `for`, `break`, `continue`, `pass`
- **Functions** — user-defined functions with closures and return values
- **Error handling** — `attempt / rescue` blocks
- **Modules** — `import` other `.luz` files
- **Helpful errors** — every error message includes the line number
- **REPL** — interactive shell for quick experimentation
- **VS Code extension** — syntax highlighting included

---

## Installation

Luz requires **Python 3.8+** and has no external dependencies.

```bash
git clone https://github.com/Elabsurdo984/luz-lang.git
cd luz-lang
```

That's it.

---

## Usage

### Interactive REPL

```bash
python main.py
```

```
Luz Interpreter v1.1 - Type 'exit' to terminate
Luz > x = 10
Luz > write(x * 2)
20
Luz > exit
```

### Run a file

```bash
python main.py program.luz
```

### VS Code syntax highlighting

Install the extension from the `vscode-luz/` folder:
1. Copy the folder to `~/.vscode/extensions/`
2. Restart VS Code

---

## Language Reference

### Types

| Type | Example | Notes |
|---|---|---|
| Integer | `42`, `-7` | Whole numbers |
| Float | `3.14`, `-0.5` | Decimal numbers |
| String | `"hello"` | Double quotes, supports escape sequences |
| Boolean | `true`, `false` | Lowercase |
| List | `[1, "two", 3.0]` | Mixed types allowed |
| Dictionary | `{"key": value}` | String or number keys |

**Escape sequences inside strings:**

| Sequence | Result |
|---|---|
| `\n` | Newline |
| `\t` | Tab |
| `\r` | Carriage return |
| `\\` | Literal backslash |
| `\"` | Literal double quote |

---

### Variables

Variables are assigned with `=`. No declaration keyword needed.

```
x = 10
name = "Luz"
items = [1, 2, 3]
data = {"score": 100}
```

---

### Operators

**Arithmetic**

| Operator | Description | Example |
|---|---|---|
| `+` | Addition / string concat | `3 + 2` → `5` |
| `-` | Subtraction | `10 - 4` → `6` |
| `*` | Multiplication / string repeat | `"ab" * 3` → `"ababab"` |
| `/` | Division (always float) | `7 / 2` → `3.5` |
| `%` | Modulo | `10 % 3` → `1` |
| `**` | Power (right-associative) | `2 ** 8` → `256` |

**Comparison**

| Operator | Description |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `<`, `>` | Less / greater than |
| `<=`, `>=` | Less / greater than or equal |

**Logical**

| Operator | Description |
|---|---|
| `and` | Logical AND |
| `or` | Logical OR |
| `not` | Logical NOT |

**Operator precedence** (highest to lowest):

```
**
* / %
+ -
== != < > <= >=
not
and
or
```

---

### Control Flow

**if / elif / else**

```
x = 15

if x > 20 {
    write("big")
} elif x > 10 {
    write("medium")
} else {
    write("small")
}
```

**while**

```
i = 0
while i < 5 {
    write(i)
    i = i + 1
}
```

**for**

Iterates from `start` to `end` (inclusive), incrementing by 1.

```
for i = 1 to 10 {
    write(i)
}
```

**break / continue / pass**

```
for i = 1 to 10 {
    if i == 3 { continue }   # skip 3
    if i == 7 { break }      # stop at 7
    write(i)
}

if true {
    pass   # placeholder for empty blocks
}
```

---

### Functions

```
function greet(name) {
    return "Hello, " + name + "!"
}

write(greet("world"))   # Hello, world!
```

Functions capture their surrounding scope (closures):

```
function make_counter() {
    count = 0
    function increment() {
        count = count + 1
        return count
    }
    return increment
}
```

---

### Collections

**Lists**

```
fruits = ["apple", "banana", "cherry"]

write(fruits[0])      # apple
write(fruits[-1])     # cherry

fruits[1] = "mango"
append(fruits, "grape")
write(len(fruits))    # 4
```

**Dictionaries**

```
person = {"name": "Alice", "age": 30}

write(person["name"])     # Alice
person["age"] = 31

write(keys(person))       # ["name", "age"]
write(values(person))     # ["Alice", 31]
```

---

### Error Handling

```
attempt {
    x = 10 / 0
} rescue (error) {
    write("Caught:", error)
}
```

Raise a custom error with `alert`:

```
function divide(a, b) {
    if b == 0 {
        alert "Cannot divide by zero"
    }
    return a / b
}

attempt {
    divide(5, 0)
} rescue (e) {
    write(e)
}
```

---

### Modules

```
import "utils.luz"

result = my_function(42)
```

- Imports run in the global scope
- Circular imports are automatically prevented

---

### Built-in Functions

**I/O**

| Function | Description |
|---|---|
| `write(...)` | Print values to stdout |
| `listen(prompt)` | Read user input. Auto-converts numbers |

**Type casting**

| Function | Description |
|---|---|
| `to_int(v)` | Convert to integer |
| `to_float(v)` | Convert to float |
| `to_str(v)` | Convert to string |
| `to_bool(v)` | Convert to boolean |
| `to_num(v)` | Convert to int or float (auto-detect) |

**Lists**

| Function | Description |
|---|---|
| `len(list)` | Number of elements |
| `append(list, value)` | Add element to end |
| `pop(list)` | Remove and return last element |
| `pop(list, index)` | Remove and return element at index |

**Dictionaries**

| Function | Description |
|---|---|
| `len(dict)` | Number of key-value pairs |
| `keys(dict)` | Returns list of keys |
| `values(dict)` | Returns list of values |
| `remove(dict, key)` | Remove key and return its value |

**Strings**

All string functions take the string as first argument.

| Function | Description | Example |
|---|---|---|
| `len(s)` | String length | `len("hi")` → `2` |
| `trim(s)` | Remove surrounding whitespace | `trim("  hi  ")` → `"hi"` |
| `uppercase(s)` | Convert to uppercase | `uppercase("hi")` → `"HI"` |
| `lowercase(s)` | Convert to lowercase | `lowercase("HI")` → `"hi"` |
| `swap(s, old, new)` | Replace all occurrences | `swap("aXb", "X", "-")` → `"a-b"` |
| `split(s, sep?)` | Split into list | `split("a,b", ",")` → `["a","b"]` |
| `join(sep, list)` | Join list into string | `join("-", ["a","b"])` → `"a-b"` |
| `contains(s, sub)` | Check if substring exists | `contains("hello", "ell")` → `true` |
| `begins(s, prefix)` | Check prefix | `begins("hello", "he")` → `true` |
| `ends(s, suffix)` | Check suffix | `ends("hello", "lo")` → `true` |
| `find(s, sub)` | Index of first occurrence, -1 if not found | `find("hello", "ll")` → `2` |
| `count(s, sub)` | Count occurrences | `count("banana", "a")` → `3` |

---

## Architecture

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

### Lexer (`luz/lexer.py`)

Converts raw source text into a flat list of tokens. Handles numbers, strings (with escape sequences), identifiers, keywords, and operators. Tracks line numbers for every token to enable helpful error messages.

### Parser (`luz/parser.py`)

Consumes the token stream and builds an **Abstract Syntax Tree (AST)** using a **recursive descent parser**. Operator precedence is enforced through nested parsing functions — each level calls the next higher-precedence level:

```
logical_or → logical_and → logical_not → comparison
          → arithmetic → term → power → factor
```

Each node type (e.g. `BinOpNode`, `IfNode`, `CallNode`) is a plain Python class defined at the top of the file.

### Interpreter (`luz/interpreter.py`)

Walks the AST using the **Visitor pattern**: `visit(node)` dynamically dispatches to `visit_IfNode`, `visit_BinOpNode`, etc.

Scope is managed through a chain of `Environment` objects — each block or function call creates a new environment linked to its parent, enabling proper variable scoping and closures.

Control flow signals (`return`, `break`, `continue`) are implemented as Python exceptions that propagate up the call stack and are caught at the appropriate level.

### Error system (`luz/exceptions.py`)

All errors inherit from `LuzError` and are grouped into four categories:

```
LuzError
├── SyntaxFault       (lexer / parser errors)
├── SemanticFault     (type errors, undefined variables, wrong arg count...)
├── RuntimeFault      (division by zero, index out of bounds...)
└── UserFault         (raised by the alert keyword)
```

Every error carries a `line` attribute that is attached automatically when the error propagates through `visit()`.

### File overview

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
├── vscode-luz/           # VS Code syntax highlighting extension
└── examples/             # Example programs
```


---

## Running Tests

```bash
python run_tests.py
```

---

## Contributing

Contributions are welcome. If you want to add a feature, fix a bug, or improve the docs:

1. Fork the repository
2. Create a branch for your change
3. Make sure the tests pass
4. Open a pull request

If you're looking for ideas, check the open issues or consider:
- Adding more built-in math functions (`abs`, `min`, `max`, `round`)
- Integer division operator (`//`)
- First-class functions
- Negative index support for lists
- More test coverage

---

## License

MIT License — see [LICENSE](LICENSE) for details.
