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

# Baixar legendas do YouTube

> Script com interface pra baixar as legendas de um canal inteiro de uma vez.

![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)
![yt--dlp](https://img.shields.io/badge/yt--dlp-latest-red?logo=youtube&logoColor=white)
![pywebview](https://img.shields.io/badge/pywebview-latest-1f6feb)
![Status](https://img.shields.io/badge/status-no%20ar-3fb950)

## O que é

Baixar legenda de vídeo em vídeo no YouTube é chato, e não tem forma nativa
de baixar todas de um canal ou playlist de uma vez. Este script resolve isso:
recebe um vídeo, um canal inteiro, uma playlist ou uma lista de URLs coladas
e baixa a legenda `.srt` de cada um, sem precisar de API key do YouTube.

## Stack

| Tecnologia | Versão | Para quê |
|---|---|---|
| Python | 3.9+ | Runtime (uso de `list[str]` como type hint no código exige 3.9+) |
| yt-dlp | sem versão fixada em `requirements.txt` | Busca e download das legendas |
| pywebview | sem versão fixada em `requirements.txt` | Janela nativa da GUI opcional (`gui.py`) |
| pythonnet | sem versão fixada; só instalado em `sys_platform == "win32"` | Backend do pywebview no Windows |
| ffmpeg | externo, não é dependência Python | Converte a legenda pro formato `.srt` |

## Requisitos

- Python 3.9 ou mais recente
- `ffmpeg` disponível no `PATH` (usado pela conversão de legenda pra `.srt`)

## Instalação

```bash
git clone https://github.com/WednyFernandes/baixar-legendas-youtube.git
cd baixar-legendas-youtube
pip install -r requirements.txt
```

## Como usar

```bash
python baixar_legendas_canal.py https://www.youtube.com/@canal/videos
```

Aceita vídeo, canal ou playlist, sozinhos ou combinados:

```bash
python baixar_legendas_canal.py https://www.youtube.com/watch?v=XXXX
python baixar_legendas_canal.py URL1 URL2 URL3
```

Saída esperada (baixando para a pasta `legendas/`, padrão de `--saida`):

```
$ python baixar_legendas_canal.py https://www.youtube.com/watch?v=XXXX
Baixado: legendas/Nome do Video.srt
```

| Flag | Padrão | Descrição |
|---|---|---|
| `urls` | obrigatório | Uma ou mais URLs: vídeo, canal (`.../videos`) ou playlist |
| `--idiomas` | `pt,pt-BR,en` | Idiomas das legendas, separados por vírgula |
| `--saida` | `legendas` | Pasta de destino dos arquivos `.srt` |
| `--auto` | desligado | Inclui legendas geradas automaticamente quando não houver legenda manual |

Também tem uma GUI local (`pywebview` + `gui.html`):

```bash
python gui.py
```

## Como funciona

O script usa `yt_dlp` diretamente e repassa a lista de URLs pra
`ydl.download(urls)` — o próprio `yt-dlp` detecta se cada URL é vídeo, canal
(`.../videos`) ou playlist e expande pra todos os vídeos correspondentes, por
isso os três casos e a lista colada usam o mesmo caminho de código. Roda com
`skip_download=True` e `writesubtitles=True`; a legenda é convertida pro
formato `.srt` via `FFmpegSubtitlesConvertor`. Vídeo sem legenda no idioma
pedido é pulado (`ignoreerrors=True`) e o download segue pros demais. A GUI
(`gui.py`) só chama as mesmas funções (`baixar_legendas`, `parse_urls`) numa
thread separada e mostra o log na janela do `pywebview`.

## Estrutura

```
baixar_legendas_canal.py   # CLI: parseia argumentos e roda o download via yt-dlp
gui.py                     # janela pywebview que chama as mesmas funções da CLI
gui.html                   # interface da GUI (HTML/Tailwind via CDN)
requirements.txt           # dependências Python
```

## Estado

Funciona pra vídeo, canal e playlist, linha de comando e GUI. Não baixa
vídeo nem áudio, só a legenda.
