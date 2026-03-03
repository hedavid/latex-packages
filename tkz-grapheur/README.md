# tkz-grapheur

> tkz-grapheur is a package to work with curves, with TikZ - tkz-grapheur un package spécifique pour travailler avec des courbes, en TikZ.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/tkz-grapheur) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `tkz-grapheur` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install tkz-grapheur
  ```

### Via TeX Live / tlmgr

```
tlmgr install tkz-grapheur
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/tkz-grapheur) (click *Code > Download ZIP*, or clone it).
2. Place `tkz-grapheur.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/tkz-grapheur/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\tkz-grapheur\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/tkz-grapheur/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{tkz-grapheur}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |