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

## Compound assignment

| Operator | Equivalent |
|---|---|
| `x += n` | `x = x + n` |
| `x -= n` | `x = x - n` |
| `x *= n` | `x = x * n` |
| `x /= n` | `x = x / n` |

```
total = 0
total += 10
total *= 2
write(total)   # 20
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

## Logical

| Operator | Description |
|---|---|
| `and` | True if both operands are true |
| `or` | True if at least one operand is true |
| `not` | Negates a boolean |

## Ternary

```
result = "yes" if condition else "no"
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
ternary (if … else)
```
