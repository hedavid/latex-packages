# ipsum

> A LaTeX package to work with multilingual Lorem Ipsum dummy texts — Un package LaTeX pour travailler avec des textes Lorem Ipsum multilingues

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/ipsum) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `ipsum` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install ipsum
  ```

### Via TeX Live / tlmgr

```
tlmgr install ipsum
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `ipsum.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/ipsum/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\ipsum\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/ipsum/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{ipsum}

% Example: insert a Lorem Ipsum paragraph in French
\ipsum<Lang=...,Type=...>[range]
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
