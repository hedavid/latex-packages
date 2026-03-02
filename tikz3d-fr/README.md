# tikz3d-fr

> A LaTeX package for working with 3D figures in TikZ — Un package LaTeX pour travailler avec des figures 3D en TikZ

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/tikz3d-fr) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `tikz3d-fr` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install tikz3d-fr
  ```

### Via TeX Live / tlmgr

```
tlmgr install tikz3d-fr
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `tikz3d-fr.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/tikz3d-fr/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\tikz3d-fr\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/tikz3d-fr/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{tikz3d-fr}

% Example: draw a 3D cube\n\Cube[...]{}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
