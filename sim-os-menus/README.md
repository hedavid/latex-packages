# sim-os-menus

> A LaTeX package to present fake OS elements (terminal, context menu, viewer) — Un package LaTeX pour présenter de faux éléments d'OS (terminal, menu contextuel, visionneuse)

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/sim-os-menus) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `sim-os-menus` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install sim-os-menus
  ```

### Via TeX Live / tlmgr

```
tlmgr install sim-os-menus
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/sim-os-menus) (click *Code > Download ZIP*, or clone it).
2. Place `sim-os-menus.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/sim-os-menus/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\sim-os-menus\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/sim-os-menus/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{sim-os-menus}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
