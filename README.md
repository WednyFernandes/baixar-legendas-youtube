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

# Baixar legendas do YouTube

Script com interface pra baixar as legendas de um canal inteiro de uma vez.

## O que é

Baixar legenda de vídeo em vídeo no YouTube é chato, e não tem forma nativa
de baixar todas de um canal ou playlist de uma vez. Este script resolve isso:
recebe um vídeo, um canal inteiro, uma playlist ou uma lista de URLs coladas
e baixa a legenda `.srt` de cada um, sem precisar de API key do YouTube.

## Como usar

```bash
git clone https://github.com/WednyFernandes/baixar-legendas-youtube.git
cd baixar-legendas-youtube
pip install -r requirements.txt
python baixar_legendas_canal.py https://www.youtube.com/@canal/videos
```

Aceita vídeo, canal ou playlist (em qualquer combinação de URLs):

```bash
python baixar_legendas_canal.py https://www.youtube.com/watch?v=XXXX
python baixar_legendas_canal.py URL1 URL2 URL3
```

| Flag | Padrão | Descrição |
|---|---|---|
| `--idiomas` | `pt,pt-BR,en` | Idiomas das legendas, separados por vírgula |
| `--saida` | `legendas` | Pasta de destino dos arquivos `.srt` |
| `--auto` | desligado | Inclui legendas geradas automaticamente quando não houver legenda manual |

Também tem uma GUI local: `python gui.py`.

Precisa de Python 3.10+ e do `ffmpeg` no `PATH` (usado pra converter a
legenda para `.srt`).

## Como funciona

O script usa `yt_dlp` diretamente e repassa a lista de URLs pra
`ydl.download(urls)` — o próprio `yt-dlp` detecta se cada URL é vídeo, canal
(`.../videos`) ou playlist e expande pra todos os vídeos correspondentes, por
isso os três casos e a lista colada usam o mesmo caminho de código. Roda com
`skip_download=True` e `writesubtitles=True`; a legenda é convertida pro
formato `.srt` via `FFmpegSubtitlesConvertor`. Vídeo sem legenda no idioma
pedido é pulado (`ignoreerrors=True`) e o download segue pros demais.

## Estado

Funciona pra vídeo, canal e playlist, linha de comando e GUI. Não baixa
vídeo nem áudio, só a legenda.

