# Collections

## Lists

A list is an ordered, mutable sequence of values. Mixed types are allowed.

```
fruits = ["apple", "banana", "cherry"]
mixed  = [1, "two", 3.0, true, null]
empty  = []
```

### Indexing

Zero-based. Reading out-of-range raises a `RuntimeFault`:

```
write(fruits[0])   # apple
write(fruits[2])   # cherry
```

### Assignment by index

```
fruits[1] = "mango"
write(fruits)   # ["apple", "mango", "cherry"]
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
| `append(list, value)` | Add element to the end (modifies in place) |
| `pop(list)` | Remove and return the last element |
| `pop(list, index)` | Remove and return the element at index |

```
nums = [10, 20, 30]
append(nums, 40)
write(len(nums))     # 4
write(pop(nums))     # 40
write(pop(nums, 0))  # 10
write(nums)          # [20, 30]
```

---

## Dictionaries

A dictionary maps keys to values. Keys must be strings or numbers.

```
person = {"name": "Alice", "age": 30}
empty  = {}
```

### Accessing values

```
write(person["name"])   # Alice
write(person["age"])    # 30
```

### Assigning values

```
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

```
write(keys(person))      # ["name", "age", "city"]
write(values(person))    # ["Alice", 31, "Madrid"]
write(remove(person, "city"))   # Madrid
write(len(person))       # 2
```
