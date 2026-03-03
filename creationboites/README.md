# CreationBoites

> A LaTeX package providing macros to create sample boxes with tcolorbox — Un package LaTeX proposant des macros pour créer des boîtes personnalisées avec tcolorbox.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/creationboites) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `CreationBoites` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install CreationBoites
  ```

### Via TeX Live / tlmgr

```
tlmgr install CreationBoites
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/creationboites) (click *Code > Download ZIP*, or clone it).
2. Place `CreationBoites.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/CreationBoites/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\CreationBoites\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/CreationBoites/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{CreationBoites}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
