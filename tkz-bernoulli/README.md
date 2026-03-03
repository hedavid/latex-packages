# tkz-bernoulli

> A LaTeX package for representing Bernoulli trees with PGF/TikZ — Un package LaTeX pour représenter des arbres de Bernoulli avec PGF/TikZ

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/tkz-bernoulli) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `tkz-bernoulli` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install tkz-bernoulli
  ```

### Via TeX Live / tlmgr

```
tlmgr install tkz-bernoulli
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/tkz-bernoulli) (click *Code > Download ZIP*, or clone it).
2. Place `tkz-bernoulli.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/tkz-bernoulli/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\tkz-bernoulli\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/tkz-bernoulli/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{tkz-bernoulli}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
