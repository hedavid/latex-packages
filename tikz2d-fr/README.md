# tikz2d-fr

> A LaTeX package to work with simplified 2D TikZ commands (French keys, freehand style, points, segments…) — Un package LaTeX pour travailler avec des commandes TikZ 2D simplifiées (clés françaises, style main levée, points, segments…)

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/tikz2d-fr) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `tikz2d-fr` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install tikz2d-fr
  ```

### Via TeX Live / tlmgr

```
tlmgr install tikz2d-fr
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `tikz2d-fr.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/tikz2d-fr/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\tikz2d-fr\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/tikz2d-fr/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{tikz2d-fr}

% Example: define and mark points\n\DefinirPoints{A/1/2, B/3/4}\n\MarquerPoints{A,B}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
