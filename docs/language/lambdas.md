# Lambdas

Lambdas are anonymous functions written inline with the `fn` keyword. They are first-class values and can be stored, passed, and returned like any other value.

## Short form

Evaluates a single expression and returns it:

```
double = fn(x) => x * 2
write(double(5))   # 10

add = fn(a, b) => a + b
write(add(3, 4))   # 7
```

## Long form

Runs a block with multiple statements. Use `return` to produce a value:

```
greet = fn(name) {
    msg = "Hello, " + name + "!"
    return msg
}

write(greet("Luz"))   # Hello, Luz!
```

## No parameters

```
say_hi = fn() => "hi!"
write(say_hi())   # hi!
```

## Passing as arguments

Lambdas are most useful when passed directly to a function:

```
function apply(f, value) {
    return f(value)
}

write(apply(fn(x) => x * x, 6))   # 36
write(apply(fn(x) => x + 10, 5))  # 15
```

## Storing in a list

```
ops = [
    fn(x) => x + 1,
    fn(x) => x * 2,
    fn(x) => x - 3
]

for op in ops {
    write(op(10))
}
# 11
# 20
# 7
```

## Closures

Lambdas capture variables from the surrounding scope at the time they are created:

```
function make_adder(n) {
    return fn(x) => x + n
}

add5 = make_adder(5)
add10 = make_adder(10)

write(add5(3))    # 8
write(add10(3))   # 13
```

## Immediately invoked

A lambda can be called right after it is defined:

```
result = fn(x) => x * x
write(result(7))   # 49
```

## Difference between `fn` and `function`

| | `function` | `fn` |
|---|---|---|
| Name | Required | None (anonymous) |
| Short form | No | `fn(x) => expr` |
| Long form | Yes | `fn(x) { body }` |
| Recursion | Yes (by name) | Not directly |
| Use case | Reusable, top-level | Inline, callbacks |
