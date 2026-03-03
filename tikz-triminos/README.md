# tikz-triminos

> A LaTeX package to create triminos with TikZ — Un package LaTeX pour créer des triminos avec TikZ

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/tikz-triminos) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `tikz-triminos` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install tikz-triminos
  ```

### Via TeX Live / tlmgr

```
tlmgr install tikz-triminos
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/tikz-triminos) (click *Code > Download ZIP*, or clone it).
2. Place `tikz-triminos.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/tikz-triminos/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\tikz-triminos\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/tikz-triminos/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{tikz-triminos}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **Inspiration** | https://schule.paul-matthies.de/Trimino.php (CC BY-NC-SA 4.0) |