# Changelog

All notable changes to Luz are documented here.
Format: `## [version] - YYYY-MM-DD` followed by categorized entries.

---

## [1.15.0] - 2026-03-22

### Added
- Pylint to CI pipeline with a minimum score of 9.0/10
- `.pylintrc` configuration silencing false positives from intentional design decisions
- Lint instructions to `CONTRIBUTING.md`

---

## [1.14.0] - 2026-03-15

### Added
- `from "module" import name` syntax for selective imports
- `import "module" as alias` syntax for aliased imports
- `finally` block in `attempt / rescue`
- `rescue` now accepts an optional error variable (can be omitted)
- Unicode escape sequences (`\uXXXX`, `\UXXXXXXXX`) in string literals
- Scientific notation support for numeric literals (`1.5e10`, `3e-4`)

### Fixed
- `for` loop now validates step direction (errors if step sign contradicts range direction)
- Recursion error messages now report the function name

---

## [1.13.0] - 2026-03-01

### Added
- Block scope for `if` and `while` — variables declared inside do not leak out
- Default function arguments now evaluate in caller scope, not closure scope
- CI test matrix across Python 3.10, 3.11, and 3.12
- 72-test pytest suite organized in 9 classes

### Fixed
- `typeof` module resolution no longer errors on built-in type names
- Scope leak: assigning to a variable no longer creates it in the wrong scope
- Circular inheritance no longer causes infinite recursion (raises `InheritanceFault`)
- Failed imports are properly deregistered so re-importing works correctly
- `len()` no longer uses a bare `except` clause

---

## [1.12.0] - 2026-02-15

### Added
- `switch / case` statement
- `match` expression with multiple value patterns per case
- Compound assignment operators: `+=`, `-=`, `*=`, `/=`
- Negative indexing for lists and strings (`list[-1]`)
- Destructuring assignment: `x, y = func()`

---

## [1.11.0] - 2026-02-01

### Added
- Multiple return values from functions
- Variadic arguments (`...args`)
- Named arguments at call sites
- Lambda expressions: `fn(x) => x * 2` and `fn(x) { body }`

---

## [1.10.0] - 2026-01-15

### Added
- Object-oriented programming: `class`, `extends`, method overriding, `super`
- `attempt / rescue` error handling and `alert` to raise errors
- Module system: `import "path"`
- Ray package manager

---
