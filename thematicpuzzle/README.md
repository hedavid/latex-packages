# thematicpuzzle

> A LaTeX package to create horizontal banners in a puzzle style — Un package LaTeX pour créer des bannières horizontales dans un style puzzle

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/thematicpuzzle) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `thematicpuzzle` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install thematicpuzzle
  ```

### Via TeX Live / tlmgr

```
tlmgr install thematicpuzzle
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `thematicpuzzle.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/thematicpuzzle/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\thematicpuzzle\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/thematicpuzzle/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{thematicpuzzle}

% Example: create a thematic puzzle banner\n\BannierePuzzle[...]{}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
