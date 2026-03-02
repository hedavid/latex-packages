# PixelArtTikz

> A LaTeX package defining commands and an environment for displaying pixel arts with TikZ — Un package LaTeX définissant des commandes et un environnement pour afficher des pixel arts avec TikZ

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/pixelarttikz) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `PixelArtTikz` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install PixelArtTikz
  ```

### Via TeX Live / tlmgr

```
tlmgr install PixelArtTikz
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `PixelArtTikz.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/PixelArtTikz/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\PixelArtTikz\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/PixelArtTikz/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{PixelArtTikz}

% Example: display a pixel art\n\begin{PixelArt}...\n\end{PixelArt}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
