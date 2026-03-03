# Scrabble

> A LaTeX package providing commands to work with a Scrabble board — Un package LaTeX proposant des commandes pour travailler avec un plateau de Scrabble

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/scrabble) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `Scrabble` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install Scrabble
  ```

### Via TeX Live / tlmgr

```
tlmgr install Scrabble
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/scrabble) (click *Code > Download ZIP*, or clone it).
2. Place `Scrabble.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/Scrabble/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\Scrabble\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/Scrabble/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{Scrabble}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| **Inspiration** | Mark Wibrow in https://tex.stackexchange.com/questions/194780/tikz-drawing-a-rectangle-with-spikes-on-borders |
| | Scrabble is a Trademark from Hasbro and Mattel |