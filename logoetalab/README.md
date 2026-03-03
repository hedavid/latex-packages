# logoetalab

> A LaTeX package to display the "Licence Ouverte Etalab 2.0" vector logo — Un package LaTeX pour afficher le logo vectoriel de la « Licence Ouverte Etalab 2.0 »

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/logoetalab) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `logoetalab` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install logoetalab
  ```

### Via TeX Live / tlmgr

```
tlmgr install logoetalab
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/logoetalab) (click *Code > Download ZIP*, or clone it).
2. Place `logoetalab.sty` and `*.pdf` files in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/logoetalab/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\logoetalab\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/logoetalab/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{logoetalab}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **License svg** | CC-BY 2.0 |