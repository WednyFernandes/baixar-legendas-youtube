#!/usr/bin/env python3
"""Baixa as legendas .srt de todos os videos de um canal do YouTube."""
import argparse
import sys

try:
    import yt_dlp
except ImportError:
    sys.exit("Instale a dependencia: pip install yt-dlp  (e tenha o ffmpeg no PATH)")


def baixar_legendas(canal_url: str, idiomas: list[str], saida: str, incluir_auto: bool, log=None) -> None:
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
        ydl.download([canal_url])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("canal", help="URL do canal (ex: https://www.youtube.com/@canal/videos)")
    parser.add_argument("--idiomas", default="pt,pt-BR,en", help="Idiomas separados por virgula")
    parser.add_argument("--saida", default="legendas", help="Pasta de destino")
    parser.add_argument("--auto", action="store_true", help="Incluir legendas geradas automaticamente (auto-caption)")
    args = parser.parse_args()

    baixar_legendas(args.canal, args.idiomas.split(","), args.saida, args.auto)
