# Collections

## Lists

A list is an ordered, mutable sequence of values.

```
fruits = ["apple", "banana", "cherry"]
mixed  = [1, "two", 3.0, true, null]
empty  = []
```

### Indexing

Zero-based. Negative indices count from the end:

```
write(fruits[0])    # apple
write(fruits[-1])   # cherry  (last element)
write(fruits[-2])   # banana
```

### Assignment by index

```
fruits[1] = "mango"
```

### Iteration

```
for fruit in fruits {
    write(fruit)
}
```

### List built-ins

| Function | Description |
|---|---|
| `len(list)` | Number of elements |
| `append(list, value)` | Add element to the end |
| `pop(list)` | Remove and return the last element |
| `pop(list, index)` | Remove and return element at index |

---

## Strings

Strings support indexing and negative indices:

```
s = "hello"
write(s[0])    # h
write(s[-1])   # o
```

---

## Dictionaries

A dictionary maps keys to values. Keys must be strings or numbers.

```
person = {"name": "Alice", "age": 30}
```

### Access and assignment

```
write(person["name"])   # Alice
person["age"] = 31
person["city"] = "Madrid"
```

### Iteration

Iterating over a dictionary yields its keys:

```
for key in person {
    write($"{key}: {person[key]}")
}
```

### Dictionary built-ins

| Function | Description |
|---|---|
| `len(dict)` | Number of key-value pairs |
| `keys(dict)` | Returns a list of all keys |
| `values(dict)` | Returns a list of all values |
| `remove(dict, key)` | Remove key and return its value |
