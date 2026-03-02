# randintlist

> A LaTeX package providing macros for creating random integer number lists between a and b, with repeating and sorting options — Un package LaTeX proposant des macros pour créer des listes d'entiers aléatoires entre a et b, avec options de répétition et de tri

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/randintlist) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `randintlist` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install randintlist
  ```

### Via TeX Live / tlmgr

```
tlmgr install randintlist
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `randintlist.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/randintlist/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\randintlist\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/randintlist/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{randintlist}

% Example: generate a list of 5 random integers between 1 and 10\n\RandIntList{5}{1}{10}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
