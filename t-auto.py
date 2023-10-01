#!/bin/python3
#
# Tradutor simples de legendas de arquivos '.srt'
#
# Modo de Uso:
# $ ./translateAuto.py -h
#
# Por oliver, 27 de setembro 2023
#

### Módulos necessários:

try:
    import deep_translator
except ModuleNotFoundError as err:
    exit(err)

import optparse
import subprocess
from os.path import (isdir)
from src.language import languages
from src.menu import banner

# Versão do programa
version = "0.0.4"

# Cores padrão
w, r, g, y, b, d_g, c, m = "\033[0m", "\033[1;31m", "\033[1;32m", "\033[1;33m", "\033[1;34m", "\033[2;32m", "\033[1;35m", "\033[1;36m"


### Traduz do idioma de origem 'source' para o 'target'

def translate_text(source, target, text):
    translate = deep_translator.GoogleTranslator()
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
    
### Traduz apenas um arquivo:

def translate_a_file(source, target, file, directory=""):
    if directory != "":
        file = f"subtitle/{file}"
        
    f = open(f"{file}")
    f_text = f.read()
    
    print(f"{w}[{b}*{w}] Translating the subtitle, this process takes a little time. Please wait{w}...\n")
    print(f"{w}[{b}*{w}] Translating from {m}{source} {w}to {m}{target}{w}...\n")
    
    translated = translate_text(source, target, f_text)
    new_name_file = f.name.replace('.srt', f'-{target}.srt')
    file_write(new_name_file, translated)

    
### Traduz todos os arquivos .srt disponíveis dentro do diretório subtitle/:

def translate_all_files(source, target, directory):
    output = subprocess.Popen([f"ls {directory}"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    files = output.stdout.read().split("\n")

    files_subtitle = []
    
    for file in files:
        extension = file.split(".")[-1]
        
        if extension == "srt":
            if(check_empty_file(f"{directory}/{file}")):
                files_subtitle.append(file)
            else:
                 print(f"{w}[{y}!{w}] The subtitle file cannot be empty {m}{directory}/{file}{w}\n")
                 
    for file in files_subtitle:
        translate_a_file(source, target, file, directory="subtitle")

    #exit(f"\n{w}[{d_g}√{w}] Process completed successfully...{d_g}OK{w}")

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
    parse.set_usage('./t-auto.py --source=<language> --target=<language> --file=<file>')
    parse.add_option("-v", "--version", action="store_true", help="Versão do Program")
    parse.add_option("-s", "--source", dest="source", help="Idioma de origem")
    parse.add_option("-t", "--target", dest="target", help="Idioma alvo")
    parse.add_option("-f", "--file", dest="file", help="Arquivo de legenda .srt")
    parse.add_option("-a", "--all", action="store_true", help="Traduz todos os arquivos de legenda .srt disponíveis dentro do diretório padrão subtitle")
    parse.add_option("-l", "--languages", action="store_true", help="Lista todos os idiomas")

    parse.version = version
    
    options, args = parse.parse_args()

    if options.source and\
         options.target and\
         options.file:

        if options.source not in languages.values() \
            or options.target not in languages.values():
            print(languages.values())
        else:
            if options.file.split('.')[-1] == "srt":

                if (check_empty_file(options.file)):
                    banner()
                    translate_a_file(options.source, options.target, options.file)
        
                else:
                    print(f"{w}[{y}!{w}] The subtitle file cannot be empty")
            else:
                print(f"{w}[{y}!{w}] .srt subtitle file is required.")
                
    elif options.source and \
         options.target and \
         options.all:
         
         if isdir("subtitle"):
            banner()
            translate_all_files(options.source, options.target, directory="subtitle")
            
         else:
            exit(f"{w}[{y}!{w}] This directory does not exist: {y}subtitle{w}")
    
    elif options.languages:
        print(f"{w}[{b}+{w}] All languages available:{w}")
        print(languages)

    elif options.version:
        print(f"{w}[+] Current version: {d_g}{parse.version}{w}")
        
    else:
        print(f"{w}[{y}!{w}] Try using the options {d_g}-h{w},{d_g}--help{w}")

options() 
