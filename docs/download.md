# Download

<div style="text-align: center; margin: 2rem 0;">
  <a href="https://github.com/Elabsurdo984/luz-lang/releases/latest/download/luz-setup.exe"
     style="background:#e65100;color:white;padding:14px 32px;border-radius:8px;font-size:1.1rem;font-weight:bold;text-decoration:none;">
    Download for Windows
  </a>
  <p style="margin-top:1rem;color:#888;">luz-setup.exe · Windows 10 or later · No dependencies</p>
</div>

### What's included

- Full Luz interpreter as a standalone executable
- `ray` package manager included
- `luz` and `ray` added to your system PATH automatically
- Standard libraries pre-installed
- No Python required

### After installing

Open a new terminal and run:

```bash
luz program.luz   # run a file
luz               # open the interactive REPL
ray install user/package   # install a package
```

### Other platforms

Linux and macOS builds are not available yet. You can run Luz from source:

```bash
git clone https://github.com/Elabsurdo984/luz-lang.git
cd luz-lang
python main.py program.luz
```

---

## Release history

| Version | Highlights |
|---|---|
| **v1.12.0** | switch/match, variadic functions, default parameters, multiple return values, ternary operator |
| **v1.10.0** | luz-random library, compound assignment (`+=` etc.), negative indexing |
| **v1.8.0** | Lambdas, OOP, format strings, modules, luz-math library, standalone installer |
