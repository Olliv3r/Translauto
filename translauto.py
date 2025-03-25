#!/usr/bin/env python3
# Tradutor de legendas SRT

import os
import sys
from deep_translator import GoogleTranslator
from deep_translator.exceptions import (
    NotValidLength, TooManyRequests, RequestError, LanguageNotSupportedException
)
from optparse import OptionParser
from src.language import languages
from src.menu import banner

VERSION = '0.1.0'

def translate(text, source='auto', target='pt'):
    """Traduz um texto."""
    try:
        return GoogleTranslator(source, target).translate(text)
    except NotValidLength:
        print("[!] Texto muito grande, traduzindo por partes...\n")
        return translate_parts(text, source, target)
    except LanguageNotSupportedException:
        raise ValueError("Idioma inválido")
    except TooManyRequests:
        raise ConnectionError("Problema de conexão (muitas requisições)")
    except RequestError:
        raise ConnectionError("Erro ao conectar-se ao serviço de tradução")

def translate_parts(text, source, target):
    """Traduz textos longos dividindo em partes menores."""
    parts = text.split("\n\n")
    return "\n\n".join(translate(part, source, target) for part in parts)

def translate_file(file_path, source, target, replace=False):
    """Traduz um arquivo SRT."""
    if not os.path.isfile(file_path):
        print(f"[X] Arquivo não encontrado: {file_path}")
        return
    
    if not file_path.endswith(".srt"):
        print(f"[X] Extensão inválida: {file_path}")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().strip()
    
    if not text:
        print(f"[X] Arquivo vazio: {file_path}")
        return
    
    print(f"[*] Traduzindo {file_path} de {source} para {target}...\n")
    translated_text = translate(text, source, target)
    write_to_file(file_path, translated_text, target, replace)

def translate_directory(directory, source, target, replace=False):
    """Traduz todos os arquivos SRT dentro de um diretório."""
    if not os.path.isdir(directory):
        print(f"[X] Diretório não encontrado: {directory}")
        return

    for file in os.listdir(directory):
        if file.endswith(".srt"):
            translate_file(os.path.join(directory, file), source, target, replace)

def write_to_file(original_file, text, target, replace):
    """Escreve o texto traduzido em um novo arquivo."""
    new_file = original_file if replace else original_file.replace(".srt", f"-{target}.srt")

    with open(new_file, "w", encoding="utf-8") as file:
        file.write(text)

    print(f"[✓] Tradução salva em {new_file}\n")

if __name__ == "__main__":
    parser = OptionParser()
    parser.set_usage("./translauto.py -s LANG_SRC -t LANG_DST -f FILE | -a")
    parser.add_option("-v", "--version", action="store_true", help="Versão do programa")
    parser.add_option("-s", "--source", dest="source", help="Idioma de origem")
    parser.add_option("-t", "--target", dest="target", help="Idioma de destino")
    parser.add_option("-f", "--file", dest="file", help="Arquivo .srt a ser traduzido")
    parser.add_option("-r", "--replace-file", action="store_true", help="Substitui arquivo original")
    parser.add_option("-a", "--all", action="store_true", help="Traduz todos os arquivos .srt no diretório padrão")
    parser.add_option("-l", "--languages", action="store_true", help="Lista idiomas disponíveis")
    
    options, _ = parser.parse_args()

    if options.version:
        print(VERSION)
    elif options.languages:
        print(languages)
    elif options.source and options.target:
        if options.file:
            translate_file(options.file, options.source, options.target, options.replace_file)
        elif options.all:
            directory = os.environ.get("T_AUTO_DIR", "subtitle")
            translate_directory(directory, options.source, options.target, options.replace_file)
        else:
            print("[X] Especifique um arquivo ou diretório para tradução.")
    else:
        parser.print_help()

