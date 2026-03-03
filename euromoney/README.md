# euromoney

> A LaTeX package to insert vectorial euro coins and banknotes, with stacking option — Un package LaTeX pour insérer des pièces et billets en euros vectoriels, avec option d'empilement.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/euromoney) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `euromoney` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install euromoney
  ```

### Via TeX Live / tlmgr

```
tlmgr install euromoney
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/euromoney) (click *Code > Download ZIP*, or clone it).
2. Place `euromoney.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/euromoney/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\euromoney\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/euromoney/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{euromoney}
```

---

## Sources & Licenses

The PDF files were converted from SVG files available on openclipart, by user *frankes*.

| Source | License |
|---|---|
| [openclipart – frankes](https://openclipart.org/artist/frankes) | CC0 1.0 Universal (Public Domain) |

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |


........: pdf converted from domain public svg (user frankes in openclipart), see https://openclipart.org/artist/frankes