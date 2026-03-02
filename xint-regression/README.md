# xint-regression

> A LaTeX package for determining classical regressions (linear, quadratic, cubic, exponential, etc.) with xint — Un package LaTeX pour déterminer des régressions classiques (linéaire, quadratique, cubique, exponentielle, etc.) avec xint

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/xint-regression) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `xint-regression` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install xint-regression
  ```

### Via TeX Live / tlmgr

```
tlmgr install xint-regression
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `xint-regression.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/xint-regression/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\xint-regression\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/xint-regression/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{xint-regression}

% Example: compute a linear regression\n\RegressionLineaire{...}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
