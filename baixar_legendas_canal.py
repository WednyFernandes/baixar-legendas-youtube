#!/usr/bin/env python3
"""Baixa as legendas .srt de videos, canais, playlists ou uma lista de URLs do YouTube."""
import argparse
import sys

try:
    import yt_dlp
except ImportError:
    sys.exit("Instale a dependencia: pip install yt-dlp  (e tenha o ffmpeg no PATH)")


def parse_urls(texto: str) -> list[str]:
    """Aceita varias URLs coladas, uma por linha (video, canal ou playlist)."""
    return [linha.strip() for linha in texto.splitlines() if linha.strip()]


def baixar_legendas(urls: list[str], idiomas: list[str], saida: str, incluir_auto: bool, log=None) -> None:
    class _Logger:
        def debug(self, msg):
            if log and not msg.startswith("[debug] "):
                log(msg)
        def warning(self, msg):
            if log:
                log(f"AVISO: {msg}")
        def error(self, msg):
            if log:
                log(f"ERRO: {msg}")

    def _hook(d):
        if log and d.get("status") == "finished":
            log(f"Baixado: {d.get('filename', '')}")

    opcoes = {
        "skip_download": True,
        "writesubtitles": True,
        "writeautomaticsub": incluir_auto,
        "subtitleslangs": idiomas,
        "subtitlesformat": "srt/best",
        "outtmpl": f"{saida}/%(title)s.%(ext)s",
        "ignoreerrors": True,
        "postprocessors": [{"key": "FFmpegSubtitlesConvertor", "format": "srt"}],
        "logger": _Logger() if log else None,
        "progress_hooks": [_hook] if log else [],
    }
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        ydl.download(urls)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("urls", nargs="+", help="Uma ou mais URLs: video, canal (.../videos) ou playlist")
    parser.add_argument("--idiomas", default="pt,pt-BR,en", help="Idiomas separados por virgula")
    parser.add_argument("--saida", default="legendas", help="Pasta de destino")
    parser.add_argument("--auto", action="store_true", help="Incluir legendas geradas automaticamente (auto-caption)")
    args = parser.parse_args()

    baixar_legendas(args.urls, args.idiomas.split(","), args.saida, args.auto)
