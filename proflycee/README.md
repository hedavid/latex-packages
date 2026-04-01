# ProfLycee

> A LaTeX package for French maths teachers in high school — Un package LaTeX pour les enseignants de mathématiques au lycée.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/proflycee) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `ProfLycee` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install ProfLycee
  ```

### Via TeX Live / tlmgr

```
tlmgr install ProfLycee
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/proflycee) (click *Code > Download ZIP*, or clone it).
2. Place `ProfLycee.sty` and all other files (`*.sty`, `*.tex` and `*.pdf`) in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/ProfLycee/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\ProfLycee\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/ProfLycee/`
3. Place the MetaPost files (`.mp`) in the appropriate directory, for example:
   - **TeX Live / Linux**: `~/texmf/metapost/ProfLycee/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\metapost\ProfLycee\`
   - **macOS (MacTeX)**: `~/Library/texmf/metapost/ProfLycee/`
4. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{ProfLycee}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later · CC0/MIT for cliparts · CC BY-SA 3.0 (from Mark Wibrow helping code) |