# JeuxCartes

> A LaTeX package with playing cards — Un package LaTeX avec des cartes à jouer.

---

## Installation

### Via MiKTeX

- **Graphically**: open the *MiKTeX Console*, go to *Packages*, search for `JeuxCartes` and click *Install*.
- **Command line**:
  ```
  miktex packages install JeuxCartes
  ```

### Via TeX Live / tlmgr

```
tlmgr install JeuxCartes
```

> On Linux, you may need to prefix with `sudo` depending on your installation.

### Manual installation

If the package is not yet available through a package manager, or if you want the latest version directly from this repository:

1. Download the repository (click *Code > Download ZIP*, or clone it).
2. Place `JeuxCartes.sty` in a directory where LaTeX can find it, for example:
   - **TeX Live / Linux**: `~/texmf/tex/latex/JeuxCartes/`
   - **MiKTeX / Windows**: `C:\Users\<user>\AppData\Roaming\MiKTeX\tex\latex\JeuxCartes\`
   - **macOS (MacTeX)**: `~/Library/texmf/tex/latex/JeuxCartes/`
3. Refresh the filename database:
   - TeX Live: `mktexlsr` or `texhash`
   - MiKTeX: `initexmf --update-fndb`

---

## Quick start

```latex
\usepackage{JeuxCartes}
```

---

## Author & License

| | |
|---|---|
| **Author** | Cédric Pierquet |
| **Email** | cpierquet@outlook.fr |
| **License** | Released under the [LaTeX Project Public License v1.3c](http://www.latex-project.org/lppl.txt) or later |

---

## Image Licenses

| Deck | License | Source |
|---|---|---|
| Poker v1 | LGPL-2.1 | [htdebeer/SVG-cards](https://github.com/htdebeer/SVG-cards) |
| Poker v2 | Public Domain | [tekeye.uk](https://tekeye.uk/playing_cards/svg-playing-cards) |
| Poker v3 | Public Domain | [me.uk/cards](https://www.me.uk/cards/) |
| Poker v4 | CC BY-SA 4.0 | [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Computer_screen_playing_cards_deck.svg) |
| Poker v5 | Public Domain | [me.uk/cards](https://www.me.uk/cards/) |
| Poker v6 | Public Domain | [vector-playing-cards](https://code.google.com/archive/p/vector-playing-cards) |
| Poker v7 | Public Domain | [me.uk/cards](https://www.me.uk/cards/) |
| Poker fr | LGPL-2.1 | [svg-cards.sourceforge.net](https://svg-cards.sourceforge.net/) |
| Poker bi | LGPL-3 | [tfbkny/blackjack](https://github.com/tfbkny/blackjack) |
| Tarot v1 | Public Domain | [freesvg.org](https://freesvg.org/deck-of-french-tarot-playing-cards) |
| Uno v1 | MIT | [eperezcosano.github.io](https://eperezcosano.github.io/uno-part1/) |
