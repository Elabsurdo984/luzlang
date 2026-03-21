# Types

Luz is dynamically typed. Every value has a runtime type that is checked when the value is used.

## Primitive types

| Type | Example | Notes |
|---|---|---|
| `int` | `42`, `-7`, `0` | Whole numbers, arbitrary size |
| `float` | `3.14`, `-0.5`, `.5` | Decimal numbers (IEEE 754) |
| `string` | `"hello"` | Double-quoted, immutable |
| `bool` | `true`, `false` | Lowercase literals |
| `null` | `null` | Represents the absence of a value |

## Collection types

| Type | Example | Notes |
|---|---|---|
| `list` | `[1, "two", 3.0]` | Ordered, mixed types allowed |
| `dict` | `{"key": value}` | String or number keys |

## Type inspection

Use `typeof()` to get the type name as a string:

```
write(typeof(42))        # int
write(typeof(3.14))      # float
write(typeof("hello"))   # string
write(typeof(true))      # bool
write(typeof(null))      # null
write(typeof([1, 2]))    # list
write(typeof({"a": 1}))  # dict
```

For objects, `typeof()` returns the class name:

```
class Dog { }
d = Dog()
write(typeof(d))   # Dog
```

## Escape sequences in strings

| Sequence | Result |
|---|---|
| `\n` | Newline |
| `\t` | Horizontal tab |
| `\r` | Carriage return |
| `\\` | Literal backslash |
| `\"` | Literal double quote |

```
write("line one\nline two")
write("column1\tcolumn2")
write("She said \"hello\"")
```

## Type casting

Use the built-in cast functions to convert between types:

| Function | Description |
|---|---|
| `to_int(v)` | Convert to integer (truncates floats) |
| `to_float(v)` | Convert to float |
| `to_str(v)` | Convert to string |
| `to_bool(v)` | Convert to boolean |
| `to_num(v)` | Convert to int or float (auto-detects from string) |

```
write(to_int(3.9))      # 3
write(to_float("2.5"))  # 2.5
write(to_str(42))       # "42"
write(to_bool(0))       # false
write(to_num("10"))     # 10
write(to_num("3.14"))   # 3.14
```

If the conversion fails, a `CastFault` is raised:

```
attempt {
    x = to_int("abc")
} rescue (e) {
    write(e)   # CastFault: cannot convert "abc" to int
}
```
