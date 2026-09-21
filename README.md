# Internet Archive search for qBittorrent

Install `internetarchive.py` without renaming it. It uses Python's standard
library plus qBittorrent's bundled search printer. No API key or account needed.

## Install

1. In qBittorrent, enable **View > Search Engine**.
2. Open **Search > Search plugins... > Install a new one > Local file**.
3. Select `internetarchive.py` and ensure **Internet Archive** is enabled.
4. Select this engine and try `big buck bunny` in **All categories**.

If qBittorrent asks for Python, install Python 3 from https://www.python.org/
and restart qBittorrent. This file is loaded by qBittorrent; do not run it
directly as a standalone application.

## Behavior

- One API request per search; up to 100 hits. Narrow the query for better results.
- Categories: all, books, movies, music, pictures, software. Archive's categories
  are broad: music includes other audio, movies includes other video.
- Supports Archive query syntax, e.g. `title:"big buck bunny"` or `collection:prelinger`.
- Results link to Archive's standard item torrent and original item page.
- Size, seeds, peers, and publication date are unknown and appear blank/unknown
  in qBittorrent. Archive item size is not a reliable torrent payload size.
- No background crawling, automatic downloads, or retries. Network failures and
  rate limits go to the search runner's stderr; try later if a search fails.
- A search hit does not guarantee a working/up-to-date torrent. If download fails,
  open the description page to check availability. Some Archive torrents are stale.
- Excludes items marked access-restricted; uses no credentials or access bypasses.

Use content in accordance with its rights and
[Internet Archive's terms](https://archive.org/about/terms).
This is an unofficial plugin, not endorsed by Internet Archive or qBittorrent.

To remove it, select **Internet Archive** in **Search plugins** and uninstall.
