# pynotebook

> A LaTeX package providing environments to recreate a Jupyter notebook (raw, markdown, code blocks) — Un package LaTeX proposant des environnements pour recréer un notebook Jupyter (blocs bruts, markdown, code)

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/pynotebook) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `pynotebook` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install pynotebook
  ```

### Via TeX Live / tlmgr

```
tlmgr install pynotebook
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `pynotebook.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/pynotebook/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\pynotebook\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/pynotebook/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{pynotebook}

% Example: create a code block\n\begin{CodeNotebook}...\n\end{CodeNotebook}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
