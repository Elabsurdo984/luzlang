# Control Flow

## if / elif / else

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

- `elif` and `else` are optional.
- Braces `{ }` are always required.

## Ternary operator

A compact inline conditional that returns a value:

```
label = "big" if x > 10 else "small"
write(label)
```

Ternaries can be chained:

```
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
```

## while

```
i = 0
while i < 5 {
    write(i)
    i += 1
}
```

## for — range loop

Iterates from `start` to `end` **inclusive**:

```
for i = 1 to 10 {
    write(i)
}
```

## for — for-each loop

Iterates over lists, string characters, or dictionary keys:

```
fruits = ["apple", "banana", "cherry"]
for fruit in fruits {
    write(fruit)
}

for ch in "hello" {
    write(ch)
}

for key in {"a": 1, "b": 2} {
    write(key)
}
```

## switch

Compares a value against multiple cases. Each case can match multiple values.

```
switch x {
    case 1 { write("one") }
    case 2, 3 { write("two or three") }
    else { write("other") }
}
```

- Cases are checked in order; only the first match runs.
- `else` is optional and acts as the fallback.
- The subject is compared with `==`.

## match

Like `switch` but is an **expression** — it returns a value.

```
label = match x {
    0 => "zero"
    1 => "one"
    2, 3 => "two or three"
    _ => "many"
}
```

- `_` is the wildcard — matches anything and must be last.
- Each arm is `pattern => expression`.
- Multiple patterns per arm: `2, 3 => "two or three"`.

## break / continue / pass

```
for i = 1 to 10 {
    if i == 5 { break }       # exit the loop
    if i == 3 { continue }    # skip to next iteration
    write(i)
}

if true {
    pass    # no-op placeholder
}
```
