# Format Strings

A format string is a string prefixed with `$` that can embed expressions inside `{ }`.

```
name = "Alice"
age = 30
write($"Hello {name}, you are {age} years old!")
```

## Syntax

```
$"text {expression} more text"
```

Any valid Luz expression can go inside `{ }`:

```
write($"2 + 2 = {2 + 2}")                  # 2 + 2 = 4
write($"uppercase: {uppercase(name)}")      # uppercase: ALICE
write($"list length: {len([1, 2, 3])}")    # list length: 3
write($"null value: {null}")               # null value: null
write($"condition: {10 > 5}")              # condition: true
```

## Nested expressions

Expressions can call functions, access attributes, do math — anything that returns a value:

```
class Point {
    function init(self, x, y) {
        self.x = x
        self.y = y
    }
}

p = Point(3, 4)
write($"Point is at ({p.x}, {p.y})")   # Point is at (3, 4)
```

## Escape sequences

Escape sequences in format strings work the same as in regular strings, but only outside `{ }`:

```
write($"line one\nline two")
write($"tab\there")
```

## Difference from regular strings

| | Regular string | Format string |
|---|---|---|
| Prefix | none | `$` |
| Embed expressions | no | yes, with `{ }` |
| Escape sequences | yes | yes (outside `{ }`) |
