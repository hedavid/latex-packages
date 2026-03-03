# TrivialPursuit

> A LaTeX package to display a Trivial Pursuit board game, with customization — Un package LaTeX pour afficher un plateau de Trivial Pursuit, avec personnalisation

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/trivialpursuit) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `TrivialPursuit` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install TrivialPursuit
  ```

### Via TeX Live / tlmgr

```
tlmgr install TrivialPursuit
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/trivialpursuit) (click *Code > Download ZIP*, or clone it).
2. Place `TrivialPursuit.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/TrivialPursuit/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\TrivialPursuit\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/TrivialPursuit/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{TrivialPursuit}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| | Trivial Pursuit is a Trademark from Hasbro |