# circularglyphs

> A LaTeX package for a circular glyph alphabet based on geometric constructions — Un package LaTeX pour un alphabet de glyphes circulaires basé sur des constructions géométriques.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/circularglyphs) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `circularglyphs` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install circularglyphs
  ```

### Via TeX Live / tlmgr

```
tlmgr install circularglyphs
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `circularglyphs.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/circularglyphs/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\circularglyphs\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/circularglyphs/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{circularglyphs}

% Example: render a word in circular glyphs
\CircGlyph[Inline]{ABCDEFG}
```

---

## Credits

|---|---|
| **Circular Glyphs alphabet** | [Irolan](https://www.deviantart.com/irolan/art/Circular-Glyphs-479352599) on DeviantArt |

---

## Author & License

|||
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |