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
- There is no limit to the number of `elif` branches.
- Braces `{ }` are always required, even for single-statement blocks.

## while

Repeats a block as long as the condition is true:

```
i = 0
while i < 5 {
    write(i)
    i = i + 1
}
```

## for — range loop

Iterates from `start` to `end` **inclusive**, incrementing by 1:

```
for i = 1 to 10 {
    write(i)
}
```

## for — for-each loop

Iterates over the elements of a list, the characters of a string, or the keys of a dictionary:

```
# List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits {
    write(fruit)
}

# String (character by character)
for ch in "hello" {
    write(ch)
}

# Dictionary (iterates over keys)
for key in {"a": 1, "b": 2} {
    write(key)
}
```

## break

Exits the innermost loop immediately:

```
for i = 1 to 10 {
    if i == 5 { break }
    write(i)
}
# prints 1 2 3 4
```

## continue

Skips the rest of the current iteration and moves to the next:

```
for i = 1 to 10 {
    if i == 3 { continue }
    write(i)
}
# prints 1 2 4 5 6 7 8 9 10
```

## pass

A no-op placeholder for empty blocks. Useful when a block is syntactically required but you have nothing to put in it yet:

```
if true {
    pass
}
```
