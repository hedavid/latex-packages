# highlightx

> A LaTeX package to highlight formulas or paragraphs with a handwriting effect — Un package LaTeX pour surligner des formules ou des paragraphes avec un effet manuscrit

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/highlightx) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `highlightx` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install highlightx
  ```

### Via TeX Live / tlmgr

```
tlmgr install highlightx
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/highlightx) (click *Code > Download ZIP*, or clone it).
2. Place `highlightx.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/highlightx/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\highlightx\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/highlightx/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{highlightx}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **Code** | Antal Spector-Zabusky (for hightlighting paragraphs) |