# tikzbrickfigurines

> A LaTeX package to draw 2D brick figurines with TikZ — Un package LaTeX pour dessiner des figurines de briques 2D avec TikZ

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/tikzbrickfigurines) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `tikzbrickfigurines` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install tikzbrickfigurines
  ```

### Via TeX Live / tlmgr

```
tlmgr install tikzbrickfigurines
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `tikzbrickfigurines.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/tikzbrickfigurines/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\tikzbrickfigurines\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/tikzbrickfigurines/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{tikzbrickfigurines}

% Example: draw a brick figurine\n\BrickFigurine[...]{}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
