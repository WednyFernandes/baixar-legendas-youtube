---
name: Baixar legendas do YouTube
name_en: YouTube subtitle downloader
type: Tool
status: no-ar
line: "Script com interface pra baixar as legendas de um canal inteiro de uma vez."
line_en: "A script with a UI to download the subtitles of an entire channel at once."
link: https://github.com/WednyFernandes/baixar-legendas-youtube
cta: github
site: true
year: 2025
tags: [python, yt-dlp, pywebview]
---

# YouTube subtitle downloader

> A script with a UI to download the subtitles of an entire channel at once.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![yt--dlp](https://img.shields.io/badge/yt--dlp-latest-red?logo=youtube&logoColor=white)
![pywebview](https://img.shields.io/badge/pywebview-latest-1f6feb)
![Status](https://img.shields.io/badge/status-live-3fb950)

## What it is

Downloading YouTube subtitles video by video is tedious, and there's no
built-in way to grab every subtitle from a whole channel or playlist at
once. This script handles that: give it a single video, a whole channel, a
playlist, or a pasted list of URLs, and it downloads the `.srt` subtitle for
each one, no YouTube API key required.

## Stack

| Technology | Version | Used for |
|---|---|---|
| Python | 3.9+ | Runtime (the code uses `list[str]` as a type hint, which requires 3.9+) |
| yt-dlp | unpinned in `requirements.txt` | Fetching and downloading subtitles |
| pywebview | unpinned in `requirements.txt` | Native window for the optional GUI (`gui.py`) |
| pythonnet | unpinned; only installed on `sys_platform == "win32"` | pywebview's backend on Windows |
| ffmpeg | external, not a Python dependency | Converts the subtitle to `.srt` |

## Requirements

- Python 3.9 or newer
- `ffmpeg` available on `PATH` (used by the subtitle-to-`.srt` conversion)

## Installation

```bash
git clone https://github.com/WednyFernandes/baixar-legendas-youtube.git
cd baixar-legendas-youtube
pip install -r requirements.txt
```

## Usage

```bash
python baixar_legendas_canal.py https://www.youtube.com/@channel/videos
```

Accepts a video, a channel, or a playlist, alone or combined:

```bash
python baixar_legendas_canal.py https://www.youtube.com/watch?v=XXXX
python baixar_legendas_canal.py URL1 URL2 URL3
```

Expected output (downloading to the `legendas/` folder, the `--saida` default):

```
$ python baixar_legendas_canal.py https://www.youtube.com/watch?v=XXXX
Baixado: legendas/Video Title.srt
```

| Flag | Default | Description |
|---|---|---|
| `urls` | required | One or more URLs: video, channel (`.../videos`), or playlist |
| `--idiomas` | `pt,pt-BR,en` | Subtitle languages, comma-separated |
| `--saida` | `legendas` | Destination folder for the `.srt` files |
| `--auto` | off | Include auto-generated subtitles when no manual one exists |

There's also a local GUI (`pywebview` + `gui.html`):

```bash
python gui.py
```

## How it works

The script calls `yt_dlp` directly, passing the list of URLs to
`ydl.download(urls)` — `yt-dlp` itself detects whether each URL is a video,
a channel (`.../videos`), or a playlist, and expands it to every matching
video, which is why all three cases and the pasted list share the same code
path. It runs with `skip_download=True` and `writesubtitles=True`; the
subtitle is converted to `.srt` via `FFmpegSubtitlesConvertor`. A video with
no subtitle in the requested language is skipped (`ignoreerrors=True`) and
the download continues with the rest. The GUI (`gui.py`) just calls the same
functions (`baixar_legendas`, `parse_urls`) on a separate thread and shows
the log in the `pywebview` window.

## Structure

```
baixar_legendas_canal.py   # CLI: parses arguments and runs the download via yt-dlp
gui.py                      # pywebview window that calls the same functions as the CLI
gui.html                    # GUI interface (HTML/Tailwind via CDN)
requirements.txt            # Python dependencies
```

## Status

Works for a single video, a channel, and a playlist, both from the command
line and the GUI. It does not download video or audio, only the subtitle.
