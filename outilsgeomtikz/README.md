# OutilsGeomTikZ

> A LaTeX package providing commands to display geometric tools using TikZ (pen, compass, rule, square, protractor…) — Un package LaTeX proposant des commandes pour afficher des outils géométriques en TikZ (stylo, compas, règle, équerre, rapporteur…)

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/outilsgeomtikz) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `OutilsGeomTikZ` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install OutilsGeomTikZ
  ```

### Via TeX Live / tlmgr

```
tlmgr install OutilsGeomTikZ
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/outilsgeomtikz) (click *Code > Download ZIP*, or clone it).
2. Place `OutilsGeomTikZ.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/OutilsGeomTikZ/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\OutilsGeomTikZ\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/OutilsGeomTikZ/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{OutilsGeomTikZ}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
