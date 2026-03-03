# coloredbelts

> A LaTeX package to insert colored belts in documents (to present skills, for example) — Un package LaTeX pour insérer des ceintures colorées dans des documents (pour présenter des compétences, par exemple).

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/coloredbelts) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `coloredbelts` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install coloredbelts
  ```

### Via TeX Live / tlmgr

```
tlmgr install coloredbelts
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/coloredbelts) (click *Code > Download ZIP*, or clone it).
2. Place `coloredbelts.sty` **and all accompanying `.pdf` files** in the same directory, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/coloredbelts/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\coloredbelts\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/coloredbelts/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{coloredbelts}
```

---

## Sources & Licenses

| Source | License |
|---|---|
| [Judo yellow belt – Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Judo_yellow_belt.svg) | CC BY-SA 3.0 |

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |