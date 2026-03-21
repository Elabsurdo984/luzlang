# Operators

## Arithmetic

| Operator | Description | Example | Result |
|---|---|---|---|
| `+` | Addition / string concat | `3 + 2` | `5` |
| `-` | Subtraction / unary negation | `10 - 4` | `6` |
| `*` | Multiplication / string repeat | `"ab" * 3` | `"ababab"` |
| `/` | Division (always float) | `7 / 2` | `3.5` |
| `//` | Integer (floor) division | `7 // 2` | `3` |
| `%` | Modulo | `10 % 3` | `1` |
| `**` | Exponentiation (right-associative) | `2 ** 8` | `256` |

### String operations

`+` concatenates two strings:

```
write("Hello" + ", " + "world!")   # Hello, world!
```

`*` repeats a string:

```
write("ha" * 3)   # hahaha
```

## Comparison

| Operator | Description |
|---|---|
| `==` | Equal |
| `!=` | Not equal |
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |

Comparison operators return `true` or `false`.

```
write(5 == 5)    # true
write(3 != 4)    # true
write(10 > 20)   # false
```

## Logical

| Operator | Description |
|---|---|
| `and` | True if both operands are true |
| `or` | True if at least one operand is true |
| `not` | Negates a boolean |

```
write(true and false)   # false
write(true or false)    # true
write(not true)         # false
```

## Operator precedence

From highest to lowest:

```
**
* / // %
+ -
== != < > <= >=
not
and
or
```

Use parentheses to override precedence:

```
write(2 + 3 * 4)     # 14  (multiplication first)
write((2 + 3) * 4)   # 20  (addition first)
```
