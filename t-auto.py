#!/bin/python3
#
# Tradutor simples de legendas de arquivos '.srt'
#
# Modo de Uso:
# $ ./translateAuto.py -h
#
# Por oliver, 27 de setembro 2023
#
#  Atualizado em 22 de outubro 2023
#

### Módulos necessários:
try:
    import deep_translator, requests
except ModuleNotFoundError as err:
    exit(err)

import optparse
import subprocess
from os.path import (isdir)
from src.language import languages
from src.menu import banner

### Versão do programa:
version = "0.0.7"

### Cores padrão:
w, r, g, y, b, d_g, c, m = "\033[0m", "\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[2;32m", "\033[1;35m", "\033[1;36m"

### Faz referencia a classe:
translate = deep_translator.GoogleTranslator()

### Checa acesso a internet:
def check_internet():
    print(f"\r{w}[{b}*{w}] {g}Checking internet access...{w}")
    try:
        requests.request('get', 'https://www.google.com', timeout=5)
        print(f"\r{w}[{b}+{w}] {g}The internet is connected!{w}")
    except requests.exceptions.ConnectionError:
        exit(f"\r{w}[{r}!{w}] {y}The internet is not connected!{w}")

### Traduz do idioma de origem 'source' para o 'target':
def translate_text(source, target, text):
    translate.source = source
    translate.target = target

    try:
        translated = translate.translate(text)
        return translated
        
    except deep_translator.exceptions.NotValidLength as err:
        return subtitle_parts(source, target, text)

### Traduz o arquivo por partes caso a legenda ultrapasse 500 caracteres:
def subtitle_parts(source, target, text):
    print(f"{w}[{y}!{w}] Subtitle too large detected. Translating in parts, this process takes a while. Please wait...{w}\n")
    
    subtitle_parts_translated = []
    subtitle_split = text.split("\n\n")
    
    for separate_paragraph in subtitle_split:
        translated = translate_text(source, target, separate_paragraph)
        subtitle_parts_translated.append(translated)

    return subtitle_parts_translated
    
    
### Traduz todos os arquivos .srt disponíveis dentro do diretório subtitle/:
def translate_all_files(source="", target="", directory="subtitle", replace_file=False):

    if not isdir(directory):
        exit(f"{w}[{y}!{w}] The default directory was not found{w}")

    output = subprocess.Popen([f"ls {directory}"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    files = output.stdout.read().split("\n")

    files_subtitle = []
    
    for file in files:
        extension = file.split(".")[-1]
 
        if extension == "srt":
            if(check_empty_file(f"{directory}/{file}")):
                files_subtitle.append(file)
                 
    for file in files_subtitle:
        translate_a_file(
            source=source, 
            target=target, 
            file=f"{directory}/{file}",
            replace_file=replace_file
        )

### Traduz apenas um arquivo:
def translate_a_file(source="", target="", file="", replace_file=False):

    if file.split('.')[-1] != "srt":
        exit(f"{w}[{y}!{w}] .srt subtitle file is required.")
        
    if not check_empty_file(file):
        exit(f"{w}[{y}!{w}] The subtitle file cannot be empty")
    
    f = open(f"{file}")
    f_text = f.read()
    
    print(f"{w}[{b}*{w}] Translating the subtitle, this process takes a little time. Please wait{w}...\n")
    print(f"{w}[{b}*{w}] Translating from {m}{source} {w}to {m}{target}{w}...\n")
    
    translated = translate_text(source, target, f_text)

    if not replace_file:
        new_name_file = f.name.replace('.srt', f'-{target}.srt')
    else:
        new_name_file = f.name
    file_write(new_name_file, translated)

### Escreve um novo arquivo traduzido:
def file_write(file, translated):
    
    if type(translated) == list:
        f = open(file, 'w')
        
        for line in translated:
            f.write(line + "\n\n")
            
        f.close()
        print(f'{w}[{g}√{w}] {g}Long translation completed successfully in {y}{f.name}{w}\n')

    else:
        f = open(file, 'w')
        f.write(translated)
        f.close()
        print(f'{w}[{g}√{w}] {g}Minimal translation completed successfully in {y}{f.name}{w}\n')

### Verifica se o arquivo estar vaziu:
def check_empty_file(file):
    file = open(file)

    if file.read() != "":
        return True
    else:
        return False

### Opçôes:
def options():
    parse = optparse.OptionParser()
    parse.description = "Traduz arquivos de legenda para qualquer idioma disponível"
    parse.set_usage('./t-auto.py -s <source_lang> -t <target_lang> -f <file>')
    parse.add_option("-v", "--version", action="store_true", help="Versão do Program")
    parse.add_option("-s", "--source", dest="source", help="Idioma de origem")
    parse.add_option("-t", "--target", dest="target", help="Idioma alvo")
    parse.add_option("-f", "--file", dest="file", help="Arquivo de legenda .srt")
    parse.add_option("-r", "--replace-file", help="Substitui o(s) arquivo(s) de origem por novo(s) traduzido(s)", action="store_true")
    parse.add_option("-a", "--all", action="store_true", help="Traduz todos os arquivos de legenda .srt disponíveis dentro do diretório padrão subtitle")
    parse.add_option("-l", "--languages", action="store_true", help="Lista todos os idiomas")

    parse.version = version 
    options, args = parse.parse_args()

    if options.source and \
        options.target and \
        options.file:
        if translate.is_language_supported(options.source) == False or \
        translate.is_language_supported(options.target) == False and \
        options.source != "auto":
            exit(f"{w}[{y}!{w}] Invalid language detected")
        else:
            if options.replace_file:
                replace_file=True
            else:
                replace_file=False

            banner() ; check_internet()

            translate_a_file(
                source=options.source, 
                target=options.target, 
                file=options.file,
                replace_file=replace_file
            )
     
    elif options.source and \
        options.target and \
        options.all:
        if translate.is_language_supported(options.source) == False or \
        translate.is_language_supported(options.target) == False and \
        options.source != "auto":
            exit(f"{w}[{y}!{w}] Invalid language detected")
        else:
            if options.replace_file:
                replace_file=True
            else:
                replace_file=False

            banner() ; check_internet()

            translate_all_files(
                source=options.source, 
                target=options.target,
                replace_file=replace_file
            )
   
    elif options.languages:
        print(f"{w}[{b}+{w}] All languages available:{w}")
        print(translate.get_supported_languages())

    elif options.version:
        print(f"{w}[+] Current version: {d_g}{parse.version}{w}")
        
    else:
        print(f"{w}[{y}!{w}] Try using the options {d_g}-h{w},{d_g}--help{w}")

if __name__ == '__main__':
    options() 
