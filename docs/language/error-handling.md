# Error Handling

## attempt / rescue

Wrap code that might fail in an `attempt` block. If an error is raised, execution jumps to the `rescue` block, where you can inspect the error message:

```
attempt {
    x = 10 / 0
} rescue (error) {
    write("Caught: " + error)
}
```

The variable in `rescue (error)` holds the error message as a string.

## alert

Raise a custom error with the `alert` keyword:

```
function divide(a, b) {
    if b == 0 {
        alert "Cannot divide by zero"
    }
    return a / b
}

attempt {
    result = divide(5, 0)
} rescue (e) {
    write(e)   # Cannot divide by zero
}
```

`alert` accepts any expression:

```
alert "Something went wrong"
alert $"Value {x} is out of range"
```

## Error types

All Luz errors fall into four categories:

| Type | Raised when |
|---|---|
| `SyntaxFault` | The source code is malformed (lexer or parser) |
| `SemanticFault` | A name is undefined, wrong number of arguments, wrong type, etc. |
| `RuntimeFault` | Division by zero, index out of bounds, invalid operation |
| `UserFault` | Raised explicitly with `alert` |
| `CastFault` | A type conversion with `to_int`, `to_float`, etc. fails |

Every error message includes the source line number.

## Nested attempt blocks

`attempt` blocks can be nested. The innermost matching `rescue` handles the error:

```
attempt {
    attempt {
        alert "inner error"
    } rescue (e) {
        write("Inner caught: " + e)
        alert "re-raised"
    }
} rescue (e) {
    write("Outer caught: " + e)
}
```

## Errors not caught

If an error propagates out of all `attempt` blocks, the interpreter prints the error and stops execution.
