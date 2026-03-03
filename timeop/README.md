# timeop

> A LaTeX package to add and subtract time information — Un package LaTeX pour additionner et soustraire des durées

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/timeop) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `timeop` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install timeop
  ```

### Via TeX Live / tlmgr

```
tlmgr install timeop
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/timeop) (click *Code > Download ZIP*, or clone it).
2. Place `timeop.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/timeop/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\timeop\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/timeop/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{timeop}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
