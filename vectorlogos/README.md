# vectorlogos

> A LaTeX package to insert vectorial logos of classic software inline, with automatic height and alignment — Un package LaTeX pour insérer des logos vectoriels de logiciels classiques en ligne, avec hauteur et alignement automatiques

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/vectorlogos) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `vectorlogos` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install vectorlogos
  ```

### Via TeX Live / tlmgr

```
tlmgr install vectorlogos
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the [repository](https://github.com/cpierquet/latex-packages/tree/main/vectorlogos) (click *Code > Download ZIP*, or clone it).
2. Place `vectorlogos.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/vectorlogos/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\vectorlogos\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/vectorlogos/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{vectorlogos}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |

## Sources

I converted the logos from their original SVG or other forms, as found on the given URLs, to PDF.

| Software         | Licence | Source                                                                                               |
|------------------|---------|------------------------------------------------------------------------------------------------------|
| Texstudio        | FREE    | <https://en.m.wikipedia.org/wiki/File:TeXstudio_Logo.svg>                                            |
| Emacs            | FREE    | <https://commons.wikimedia.org/wiki/File:EmacsIcon.svg>                                              |
| Emacs alt        | FREE    | <https://fr.m.wikipedia.org/wiki/Fichier:Emacs-logo.svg>                                             |
| Geogebra         | CC30    | <https://wiki.geogebra.org/en/File:Geogebra-logo-name.svg>                                           |
| Texmaker         | FREE    | <https://en.wikipedia.org/wiki/File:TeXmaker_Logo.svg>                                               |
| Texmaker old     | FREE    | <https://en.wikipedia.org/wiki/File:TeXmaker_New_Logo.svg>                                           |
| Scratch          | Public  | <https://commons.wikimedia.org/wiki/File:Scratchlogo.svg>                                            |
| Scratch alt      | Public  | <https://commons.wikimedia.org/wiki/File:Scratchlogo.svg>                                            |
| Scratch cat      | CC40    | <https://fr.scratch-wiki.info/wiki/Fichier:Scratch_Cat_(cat-a).svg>                                  |
| Geogebra icon    | CC30    | <https://fr.m.wikipedia.org/wiki/Fichier:Geogebra.svg>                                               |
| MikTex logo      | Public  | <https://fr.wikipedia.org/wiki/Fichier:Logo_MiKTeX.svg>                                              |
| Miktex icons     | FREE    | <https://github.com/MiKTeX/miktex/tree/next/Resources/Icons/MiKTeX/scalable/apps>                    |
| CTAN Lion        | FREE    | CTAN lion drawing by Duane Bibby                                                                     |
| LaTeX project    | CC40    | <https://github.com/latex3/latex3.github.io/tree/ba511d2fd43dc08ad301e31b2a32c472b252b76b/_site/img> |
|                  |         | from Jonas Jacek (<https://www.j15k.com/>)                                                           |
| TeXworks         | GPL2    | <https://github.com/TeXworks/texworks/blob/main/res/images/TeXworks.png>                             |
