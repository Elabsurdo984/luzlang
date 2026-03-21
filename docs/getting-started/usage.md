# Usage

## Interactive REPL

Run `main.py` with no arguments to open the interactive shell:

```bash
python main.py
```

```
Luz Interpreter v1.1 - Type 'exit' to terminate
Luz > x = 10
Luz > write(x * 2)
20
Luz > name = "world"
Luz > write($"Hello {name}!")
Hello world!
Luz > exit
```

The REPL evaluates one statement at a time. Multi-line constructs (functions, classes, loops) are not supported in the REPL — use a file for those.

## Run a file

```bash
python main.py program.luz
```

Any `.luz` file can be executed this way. The interpreter runs the file from top to bottom and exits when it reaches the end.

## Run the test suite

```bash
python tests/test_suite.py
```

All built-in tests will run and report pass/fail.
