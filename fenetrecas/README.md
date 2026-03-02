# FenetreCas

> A LaTeX package providing commands to display CAS-like windows (Xcas or GeoGebra) in TikZ — Un package LaTeX proposant des commandes pour afficher des fenêtres type Xcas ou GeoGebra en TikZ.

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/fenetrecas) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `FenetreCas` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install FenetreCas
  ```

### Via TeX Live / tlmgr

```
tlmgr install FenetreCas
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `FenetreCas.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/FenetreCas/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\FenetreCas\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/FenetreCas/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{FenetreCas}

% Example: display an Xcas-like window
\LigneCalculsGeogebra{\sffamily g(x)=4/(1+e\textasciicircum(-k x))}{$\rightarrow$ \: $\mathsf{g(x)=\dfrac{4}{e^{-kx}+1}}$}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
