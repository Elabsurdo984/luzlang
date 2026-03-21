# Luz Language — VS Code Extension

Full language support for the [Luz programming language](https://elabsurdo984.github.io/luz-lang/).

## Features

### Syntax highlighting
Keywords, strings, format strings, numbers, comments, operators and more are all highlighted.

### Autocompletion
- All built-in functions (`write`, `len`, `append`, `sqrt`, `mean`...)
- All keywords (`if`, `while`, `for`, `class`, `function`...)
- Variables, functions and classes defined in the current file

### Error detection
Syntax errors are underlined in red as soon as you save the file.

![Error detection](https://raw.githubusercontent.com/Elabsurdo984/luz-lang/master/img/icon.png)

### Hover documentation
Hover over any built-in function to see its signature and description.

### Snippets

| Prefix | Expands to |
|---|---|
| `function` | Function definition |
| `if` | If statement |
| `ife` | If / else |
| `ifee` | If / elif / else |
| `while` | While loop |
| `for` | For range loop |
| `fore` | For each loop |
| `class` | Class definition |
| `classe` | Class with inheritance |
| `method` | Class method |
| `attempt` | Attempt / rescue block |
| `fn` | Lambda short form |
| `fnb` | Lambda long form |
| `import` | Import statement |
| `fs` | Format string |

## Requirements

For error detection to work, **Luz must be installed** and available in your PATH.

Download the installer at **[elabsurdo984.github.io/luz-lang/download](https://elabsurdo984.github.io/luz-lang/download/)**.

## Extension settings

| Setting | Default | Description |
|---|---|---|
| `luz.executablePath` | `luz` | Path to the luz executable |

## Quick example

```
import "math"

class Circle {
    function init(self, radius) {
        self.radius = radius
    }
    function area(self) {
        return PI * self.radius * self.radius
    }
}

c = Circle(5)
write($"Area: {round(c.area(), 2)}")
```

## Links

- [Language documentation](https://elabsurdo984.github.io/luz-lang/)
- [GitHub repository](https://github.com/Elabsurdo984/luz-lang)
- [Report an issue](https://github.com/Elabsurdo984/luz-lang/issues)
