# Download

<div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin:2rem 0;">
  <div style="text-align:center;">
    <a id="win-btn" href="https://github.com/Elabsurdo984/luz-lang/releases/latest"
       style="display:inline-block;background:#e65100;color:white;padding:14px 32px;border-radius:8px;font-size:1.1rem;font-weight:bold;text-decoration:none;">
      🪟 Download for Windows
    </a>
    <p style="margin-top:0.6rem;color:#888;font-size:0.9rem;" id="win-info">Installer · No dependencies</p>
  </div>
  <div style="text-align:center;">
    <a id="linux-btn" href="https://github.com/Elabsurdo984/luz-lang/releases/latest"
       style="display:inline-block;background:#37474f;color:white;padding:14px 32px;border-radius:8px;font-size:1.1rem;font-weight:bold;text-decoration:none;">
      🐧 Download for Linux
    </a>
    <p style="margin-top:0.6rem;color:#888;font-size:0.9rem;" id="linux-info">tar.gz · luz + ray binaries</p>
  </div>
</div>

<script>
const API = "https://api.github.com/repos/Elabsurdo984/luz-lang/releases";
fetch(API)
  .then(r => r.json())
  .then(releases => {
    const winRelease = releases.find(r => r.tag_name.startsWith("win-v"));
    const linuxRelease = releases.find(r => r.tag_name.startsWith("linux-v"));

    if (winRelease) {
      const asset = winRelease.assets.find(a => a.name.endsWith("-setup.exe"));
      if (asset) {
        document.getElementById("win-btn").href = asset.browser_download_url;
        document.getElementById("win-info").textContent = winRelease.tag_name + " · No dependencies";
      }
    }

    if (linuxRelease) {
      const asset = linuxRelease.assets.find(a => a.name.endsWith(".tar.gz"));
      if (asset) {
        document.getElementById("linux-btn").href = asset.browser_download_url;
        document.getElementById("linux-info").textContent = linuxRelease.tag_name + " · luz + ray binaries";
      }
    }
  });
</script>

### Windows — What's included

- Full Luz interpreter (`luz.exe`)
- `ray` package manager (`ray.exe`)
- `luz` and `ray` added to your system PATH automatically
- Standard libraries pre-installed (`luz-math`, `luz-random`, `luz-io`, `luz-system`)
- No Python required

### Linux — Setup after download

```bash
tar -xzf luz-*-linux.tar.gz
sudo mv luz ray /usr/local/bin/
luz program.luz
```

### After installing

```bash
luz program.luz        # run a file
luz                    # open the interactive REPL
ray install user/pkg   # install a package
```

---

## Release history

| Version | Highlights |
|---|---|
| **v1.14.0** | File I/O built-ins, luz-io library, luz-system library, Linux binary |
| **v1.13.0** | File I/O built-ins, luz-io library, ternary fix |
| **v1.12.0** | switch/match, variadic functions, default parameters, multiple return values, ternary operator |
| **v1.10.0** | luz-random library, compound assignment (`+=` etc.), negative indexing |
| **v1.8.0** | Lambdas, OOP, format strings, modules, luz-math library, standalone installer |
