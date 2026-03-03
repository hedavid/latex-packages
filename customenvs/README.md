# customenvs

> A LaTeX package providing custom environments (MCQ, list with picked items, …) — Un package LaTeX proposant des environnements personnalisés (QCM, listes à compléter, …).

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/customenvs) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `customenvs` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install customenvs
  ```

### Via TeX Live / tlmgr

```
tlmgr install customenvs
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/customenvs) (click *Code > Download ZIP*, or clone it).
2. Place all `*.sty` and `*.pdf` files in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/customenvs/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\customenvs\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/customenvs/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{customenvs}
```

---

## Sources & Licenses

| Source | License |
|---|---|
| [tex.stackexchange.com – fancy bordered text](https://tex.stackexchange.com/questions/504092/replicating-a-fancy-bordered-text-style-in-latex/504145#504145) | CC BY-SA 4.0 |
| [svgrepo.com – Education Vectors](https://www.svgrepo.com/collection/education-vectors/) | CC BY |
| [svgrepo.com – Design 8](https://www.svgrepo.com/collection/design-8/) | CC 0 |
| [Bootstrap](https://getbootstrap.com) | MIT |
| [solar-icon-react](https://github.com/itstor/solar-icon-react) | MIT |

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |