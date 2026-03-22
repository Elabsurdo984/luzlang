# Functions

## Defining a function

```
function greet(name) {
    return "Hello, " + name + "!"
}

write(greet("world"))   # Hello, world!
```

- `return` exits the function with a value.
- A function that reaches the end without a `return` returns `null`.

## Default parameters

Parameters can have a default value. All required parameters must come before defaults.

```
function greet(name, greeting = "Hello") {
    write($"{greeting}, {name}!")
}

greet("Alice")             # Hello, Alice!
greet("Bob", "Hi")         # Hi, Bob!
```

```
function connect(host, port = 8080, secure = false) {
    write($"{host}:{port} secure={secure}")
}

connect("localhost")                # localhost:8080 secure=false
connect("example.com", 443, true)   # example.com:443 secure=true
```

## Variadic functions

A `...name` parameter collects all extra arguments into a list. It must be the last parameter.

```
function sum(...nums) {
    total = 0
    for n in nums { total += n }
    return total
}

write(sum(1, 2, 3))         # 6
write(sum(10, 20, 30, 40))  # 100
write(sum())                # 0
```

Variadic can be combined with regular parameters:

```
function log(level, ...messages) {
    for msg in messages {
        write($"[{level}] {msg}")
    }
}

log("INFO", "Server started", "Ready")
```

## Multiple return values

A function can return multiple values. Use destructuring assignment to unpack them.

```
function min_max(a, b) {
    if a < b { return a, b }
    else      { return b, a }
}

lo, hi = min_max(8, 3)
write(lo)   # 3
write(hi)   # 8
```

```
function coords() {
    return 4, 7, 9
}

x, y, z = coords()
```

## Functions as values

Functions are first-class values — they can be stored and passed as arguments:

```
function double(x) {
    return x * 2
}

f = double
write(f(5))   # 10
```

## Closures

Inner functions capture variables from the enclosing scope:

```
function make_counter() {
    count = 0
    function increment() {
        count = count + 1
        return count
    }
    return increment
}

counter = make_counter()
write(counter())   # 1
write(counter())   # 2
write(counter())   # 3
```

## Recursion

```
function factorial(n) {
    if n <= 1 { return 1 }
    return n * factorial(n - 1)
}

write(factorial(6))   # 720
```

## Higher-order functions

```
function apply_twice(f, x) {
    return f(f(x))
}

write(apply_twice(fn(x) => x * 2, 3))   # 12
```
