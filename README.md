# Block Burst 🟦🟥🟨

A Block Blast!-style block puzzle game built as an iOS-friendly web app — no
frameworks, no build step, just open `index.html`.

## How to play

- Drag pieces from the tray onto the 8×8 board.
- Fill a complete row or column to clear it.
- Clear lines back-to-back to build a **combo multiplier** for bonus points.
- The game ends when none of your remaining pieces fit on the board.

## Features

- Touch-first controls (pointer events, drag lift so your finger doesn't hide
  the piece), works with mouse too.
- Placement preview with highlight of lines that would clear.
- Score, combo banner, floating point pop-ups, and persistent best score
  (localStorage).
- Clear/drop animations and a game-over screen with restart.
- PWA: web app manifest, service worker for offline play, and Apple touch
  icons — **Add to Home Screen** on iOS for a fullscreen, native-feeling app.

## Run it

Serve the folder with any static server, e.g.:

```sh
python3 -m http.server 8000
```

then open `http://localhost:8000` (or host it anywhere, like GitHub Pages).
On an iPhone, open it in Safari and use **Share → Add to Home Screen**.

## Files

- `index.html` — the entire game (markup, styles, logic)
- `manifest.json` — PWA manifest
- `sw.js` — service worker (offline cache)
- `icon-180.png`, `icon-512.png` — app icons
- `make_icons.py` — regenerates the icons (pure-Python PNG writer, no deps)
