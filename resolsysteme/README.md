# ResolSysteme

> A LaTeX package providing commands to perform calculations on small (2×2, 3×3, 4×4) linear systems — Un package LaTeX proposant des commandes pour effectuer des calculs sur de petits systèmes linéaires (2×2, 3×3, 4×4)

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/resolsysteme) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `ResolSysteme` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install ResolSysteme
  ```

### Via TeX Live / tlmgr

```
tlmgr install ResolSysteme
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `ResolSysteme.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/ResolSysteme/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\ResolSysteme\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/ResolSysteme/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{ResolSysteme}

% Example: solve a 2x2 linear system\n\SolutionSysteme{1}{2}{3}{4}{5}{6}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
