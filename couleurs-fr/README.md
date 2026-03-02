# couleurs-fr

> A LaTeX package providing colours with French names — Un package LaTeX proposant des couleurs avec des noms en français.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/couleurs-fr) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `couleurs-fr` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install couleurs-fr
  ```

### Via TeX Live / tlmgr

```
tlmgr install couleurs-fr
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `couleurs-fr.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/couleurs-fr/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\couleurs-fr\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/couleurs-fr/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{couleurs-fr}

% Example: use a French colour name
\textcolor{RougeTomate}{Mon texte en rouge tomate}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
