# TangramTikZ

> A LaTeX package for creating tangram puzzles with TikZ — Un package LaTeX pour créer des puzzles tangram avec TikZ

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/tangramtikz) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `TangramTikZ` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install TangramTikZ
  ```

### Via TeX Live / tlmgr

```
tlmgr install TangramTikZ
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `TangramTikZ.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/TangramTikZ/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\TangramTikZ\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/TangramTikZ/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{TangramTikZ}

% Example: display a tangram puzzle\n\TangramPuzzle[...]{}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
