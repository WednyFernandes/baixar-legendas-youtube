# baixar-legendas-youtube

**Download every SRT subtitle from all videos of a YouTube channel — Python script + optional desktop GUI.**

A thin, focused wrapper around [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) that enumerates every video on a YouTube channel and saves each video's subtitles (manual or auto-generated) as `.srt` files, in the languages you choose. No YouTube API key required.

> Also known as: youtube subtitle downloader, bulk srt downloader, download captions from a youtube channel, extrair legendas de canal do youtube em python.

---

## Recursos / Features

- Baixa as legendas de **todos os vídeos de um canal** de uma vez (passe a URL do canal, não vídeo por vídeo).
- Converte para **`.srt`**, com escolha de idioma(s) (ex: `pt`, `pt-BR`, `en`).
- Opção de incluir **legendas geradas automaticamente** quando não há legenda manual.
- Não baixa vídeo nem áudio — só o texto da legenda (`--skip-download`).
- **Duas formas de uso**: linha de comando (`baixar_legendas_canal.py`) ou GUI local (`gui.py`, pywebview + Tailwind).

## Requisitos

- Python 3.10+
- [`ffmpeg`](https://ffmpeg.org/download.html) no `PATH` (usado para converter a legenda para `.srt`)
- Dependências Python: `pip install -r requirements.txt`

## Instalação

```bash
git clone https://github.com/WednyFernandes/baixar-legendas-youtube.git
cd baixar-legendas-youtube
pip install -r requirements.txt
```

## Uso — linha de comando

```bash
python baixar_legendas_canal.py https://www.youtube.com/@canal/videos
```

Opções:

| Flag | Padrão | Descrição |
|---|---|---|
| `--idiomas` | `pt,pt-BR,en` | Idiomas das legendas, separados por vírgula |
| `--saida` | `legendas` | Pasta de destino dos arquivos `.srt` |
| `--auto` | desligado | Inclui legendas geradas automaticamente (auto-caption) quando não houver legenda manual |

Exemplo baixando só inglês, incluindo auto-legendas, em uma pasta específica:

```bash
python baixar_legendas_canal.py https://www.youtube.com/@canal/videos --idiomas en --auto --saida ./out
```

## Uso — GUI

```bash
python gui.py
```

Abre uma janela local (pywebview) com campos para URL do canal, idiomas, pasta de destino e a opção de incluir legendas automáticas, com log de progresso em tempo real.

## Como funciona

O script usa a biblioteca `yt_dlp` diretamente: passa a URL do canal (ex: `.../@canal/videos`), que o `yt-dlp` expande automaticamente para todos os vídeos da playlist do canal, com `skip_download=True` e `writesubtitles=True`. A legenda é convertida para `.srt` via `FFmpegSubtitlesConvertor`.

## FAQ

**Precisa de API key do YouTube?**
Não. Tudo é feito via `yt-dlp`, sem autenticação.

**Funciona com Shorts e lives encerradas?**
Sim, qualquer vídeo listado na aba `/videos` (ou playlist) do canal.

**E se o vídeo não tiver legenda em nenhum dos idiomas pedidos?**
Ele é pulado (`ignoreerrors: True`) e o download continua para os demais vídeos.

**Baixa o vídeo também?**
Não, apenas a legenda — `skip_download` está sempre ativo.

## Aviso

Baixe apenas legendas de conteúdo que você tem permissão de usar, respeitando os Termos de Serviço do YouTube e direitos autorais dos criadores.
