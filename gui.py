#!/usr/bin/env python3
"""GUI basica (pywebview + Tailwind) para baixar_legendas_canal.py."""
import threading
from pathlib import Path

import webview

from baixar_legendas_canal import baixar_legendas, parse_urls


class Api:
    window: webview.Window = None

    def escolher_pasta(self):
        resultado = self.window.create_file_dialog(webview.FOLDER_DIALOG)
        return resultado[0] if resultado else None

    def baixar(self, urls_texto, idiomas, saida, auto):
        threading.Thread(target=self._rodar, args=(urls_texto, idiomas, saida, auto), daemon=True).start()

    def _rodar(self, urls_texto, idiomas, saida, auto):
        log = lambda msg: self.window.evaluate_js(f"appendLog({msg!r})")
        try:
            urls = parse_urls(urls_texto)
            if not urls:
                log("Cole ao menos uma URL (video, canal, playlist ou lista).")
                return
            langs = [i.strip() for i in idiomas.split(",") if i.strip()]
            baixar_legendas(urls, langs, saida, auto, log=log)
            log("Concluido.")
        except Exception as e:
            log(f"Erro: {e}")
        finally:
            self.window.evaluate_js("setRunning(false)")


if __name__ == "__main__":
    api = Api()
    api.window = webview.create_window(
        "Legendas do canal",
        str(Path(__file__).with_name("gui.html")),
        js_api=api,
        width=560,
        height=720,
    )
    webview.start()
