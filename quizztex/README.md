# quizztex

> A LaTeX package to create quizzes in the style of TV shows ("Who Wants to Be a Millionaire?") — Un package LaTeX pour créer des quiz dans le style d'émissions TV (« Qui veut gagner des millions ? »)

---

## Installation

The package is available on [CTAN](https://ctan.org/pkg/quizztex) and can be installed via your LaTeX distribution's package manager.

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `quizztex` and click *Install*.
- **Command line**:
  ```
  mpm.exe --install quizztex
  ```

### Via TeX Live / tlmgr

```
tlmgr install quizztex
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `quizztex.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/quizztex/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\quizztex\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/quizztex/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{quizztex}

% Example: create a quiz question\n\Question{...}{A}{B}{C}{D}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |
| | 'Who Wants to Be a Millionaire ?' is a Trademark from Sony Pictures Television. |
| | 'Tout le monde veut prendre sa place' is a Tradematk from Air Productions |