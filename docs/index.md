<p align="center">
  <img src="img/icon.png" alt="Luz logo" width="676" height="369">
</p>

# Luz Programming Language

**Luz** is a lightweight, interpreted programming language written in Python. It is designed to be simple, readable, and easy to learn.

```
name = listen("What is your name? ")
write($"Hello {name}!")

for i = 1 to 5 {
    if even(i) {
        write($"{i} is even")
    } else {
        write($"{i} is odd")
    }
}
```

## Why Luz?

- **No boilerplate** — variables need no declaration keyword, blocks use `{ }`
- **Readable syntax** — keywords read like English (`for i = 1 to 10`, `attempt / rescue`)
- **Full OOP** — classes, inheritance, method overriding, `super`
- **First-class functions** — lambdas, closures, higher-order functions
- **Helpful errors** — every error includes the source line number
- **Zero dependencies** — just Python 3.8+

## Quick Example

```
class Animal {
    function init(self, name) {
        self.name = name
    }
    function speak(self) {
        write($"{self.name} says hello!")
    }
}

class Dog extends Animal {
    function speak(self) {
        super.speak()
        write("(woof!)")
    }
}

d = Dog("Rex")
d.speak()
```

## Features at a glance

| Feature | Syntax |
|---|---|
| Variable | `x = 10` |
| Format string | `$"Hello {name}"` |
| For range | `for i = 1 to 10 { }` |
| For each | `for item in list { }` |
| Lambda | `fn(x) => x * 2` |
| Class | `class Dog extends Animal { }` |
| Error handling | `attempt { } rescue (e) { }` |
| Import | `import "utils.luz"` |

## Download

<div style="text-align: center; margin: 1.5rem 0;">
  <a id="download-btn" href="https://github.com/Elabsurdo984/luz-lang/releases/latest"
     style="background:#e65100;color:white;padding:12px 28px;border-radius:8px;font-size:1rem;font-weight:bold;text-decoration:none;">
    Download
  </a>
  <p style="margin-top:0.75rem;color:#888;font-size:0.9rem;" id="download-info">No Python required</p>
</div>

<script>
fetch("https://api.github.com/repos/Elabsurdo984/luz-lang/releases/latest")
  .then(r => r.json())
  .then(data => {
    if (!data.assets) return;
    const isLinux = navigator.platform.toLowerCase().includes("linux");
    const win = data.assets.find(a => a.name.endsWith("-setup.exe"));
    const linux = data.assets.find(a => a.name.includes("linux") && a.name.endsWith(".tar.gz"));
    const asset = isLinux ? (linux || win) : (win || linux);
    if (asset) {
      const label = asset.name.endsWith(".exe") ? "🪟 Download for Windows" : "🐧 Download for Linux";
      document.getElementById("download-btn").href = asset.browser_download_url;
      document.getElementById("download-btn").textContent = label;
      document.getElementById("download-info").textContent = asset.name + " · No Python required";
    }
  });
</script>

## Get Started

Download the installer above, or head to [Installation](getting-started/installation.md) to run from source. Jump straight into the [Language Reference](language/types.md) to learn the syntax.
