# Functions

## Defining a function

```
function greet(name) {
    return "Hello, " + name + "!"
}

write(greet("world"))   # Hello, world!
```

- Parameters are positional — Luz has no keyword or default arguments.
- `return` exits the function with a value.
- A function that reaches the end without a `return` returns `null`.

## Multiple parameters

```
function add(a, b) {
    return a + b
}

write(add(3, 4))   # 7
```

## Functions as values

Functions are first-class values. They can be stored in variables and passed as arguments:

```
function double(x) {
    return x * 2
}

f = double
write(f(5))   # 10
```

## Nested functions

Functions can be defined inside other functions:

```
function outer() {
    function inner() {
        return "from inner"
    }
    return inner()
}

write(outer())   # from inner
```

## Closures

Inner functions capture variables from their enclosing scope. The captured variable is read at call time, not at definition time:

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

A function that takes another function as an argument:

```
function apply_twice(f, x) {
    return f(f(x))
}

function double(x) {
    return x * 2
}

write(apply_twice(double, 3))   # 12
```
