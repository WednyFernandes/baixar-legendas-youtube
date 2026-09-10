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
tags: [python, youtube]
---

# YouTube subtitle downloader

A script with a UI to download the subtitles of an entire channel at once.

## What it is

Downloading YouTube subtitles one video at a time is tedious, and there's no
native way to grab all of them from a channel or playlist at once. This
script does that: give it a video, a whole channel, a playlist, or a pasted
list of URLs, and it downloads the `.srt` subtitle for each one — no YouTube
API key required.

## How to use it

```bash
git clone https://github.com/WednyFernandes/baixar-legendas-youtube.git
cd baixar-legendas-youtube
pip install -r requirements.txt
python baixar_legendas_canal.py https://www.youtube.com/@canal/videos
```

Accepts a video, a channel, or a playlist (in any combination of URLs):

```bash
python baixar_legendas_canal.py https://www.youtube.com/watch?v=XXXX
python baixar_legendas_canal.py URL1 URL2 URL3
```

| Flag | Default | Description |
|---|---|---|
| `--idiomas` | `pt,pt-BR,en` | Subtitle languages, comma-separated |
| `--saida` | `legendas` | Output folder for the `.srt` files |
| `--auto` | off | Include auto-generated captions when there's no manual subtitle |

There's also a local GUI: `python gui.py`.

Requires Python 3.10+ and `ffmpeg` on the `PATH` (used to convert the
subtitle to `.srt`).

## How it works

The script uses `yt_dlp` directly and passes the list of URLs to
`ydl.download(urls)` — `yt-dlp` itself detects whether each URL is a video, a
channel (`.../videos`), or a playlist, and expands it to every matching
video, which is why all three cases and the pasted list share the same code
path. It runs with `skip_download=True` and `writesubtitles=True`; the
subtitle is converted to `.srt` via `FFmpegSubtitlesConvertor`. A video with
no subtitle in the requested language is skipped (`ignoreerrors=True`) and
the download continues for the rest.

## State

Works for video, channel, and playlist, both from the command line and the
GUI. Doesn't download the video or audio, only the subtitle.
