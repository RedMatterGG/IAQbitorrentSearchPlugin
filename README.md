# Internet Archive search for qBittorrent

Install `internetarchive.py` without renaming it. It uses Python's standard
library plus qBittorrent's bundled search printer. No API key or account needed.

## Install

1. In qBittorrent, enable **View > Search Engine**.
2. Open **Search > Search plugins... > Install a new one > Local file**.
3. Select `internetarchive.py` and ensure **Internet Archive** is enabled.

If qBittorrent asks for Python, install Python 3 from https://www.python.org/
and restart qBittorrent. This file is loaded by qBittorrent; do not run it
directly as a standalone application.

## Behavior

- 100 results per api request.
- Categories: all, books, movies, music, pictures, software. Archive's categories
  are broad: music includes other audio, movies includes other video.
- Supports Archive query syntax, e.g. `title:"big buck bunny"` or `collection:prelinger`.
- Results link to Archive's standard item torrent and original item page.
- Excludes items marked access-restricted; uses no credentials or access bypasses.

Use content in accordance with its rights and
[Internet Archive's terms](https://archive.org/about/terms).
This is an unofficial plugin, not endorsed by Internet Archive or qBittorrent.
