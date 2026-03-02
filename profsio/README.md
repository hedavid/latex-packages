# ProfSio

> A LaTeX package for French maths teachers in BTS SIO — Un package LaTeX pour les enseignants de mathématiques en BTS SIO.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/profsio) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `ProfSio` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install ProfSio
  ```

### Via TeX Live / tlmgr

```
tlmgr install ProfSio
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `ProfSio.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/ProfSio/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\ProfSio\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/ProfSio/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{ProfSio}

% Example: draw a Karnaugh map
\TableauKarnaugh[...]{}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |