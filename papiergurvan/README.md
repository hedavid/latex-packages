# PapierGurvan

> A LaTeX package to display Gurvan grids or full Gurvan pages, with the option to write on lines — Un package LaTeX pour afficher des grilles ou des pages Gurvan, avec possibilité d'écrire sur les lignes

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/papiergurvan) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `PapierGurvan` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install PapierGurvan
  ```

### Via TeX Live / tlmgr

```
tlmgr install PapierGurvan
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `PapierGurvan.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/PapierGurvan/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\PapierGurvan\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/PapierGurvan/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{PapierGurvan}

% Example: display a Gurvan grid\n\GrilleGurvan[...]{}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **Author of paper** | http://www.sos-ecriture.fr/2014/10/papier-gurvan.html |