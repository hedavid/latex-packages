# calculatoritems

> A LaTeX package to insert menus/items for classic calculators — Un package LaTeX pour insérer des menus/touches de calculatrices classiques.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/calculatoritems) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `calculatoritems` and click *Install*.
- **Command line**:
  ```
  miktex packages install calculatoritems
  ```

### Via TeX Live / tlmgr

```
tlmgr install calculatoritems
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `calculatoritems.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/calculatoritems/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\calculatoritems\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/calculatoritems/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{calculatoritems}

% Example: insert a NumWorks menu item
\CalcItemMenu[model=nwks,type=bmenu,rightsymb=\nwkstri,len=12,font\fontNWKS]{X predict}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |