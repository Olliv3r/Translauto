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

# Versão do programa
version = "0.0.2"

### Traduz o arquivo por partes:

def subtitle_parts(source, target, text):
    subtitle_parts_translated = []
    subtitle_split = text.split("\n\n")

    for separate_paragraph in subtitle_split:
        translated = deep_translator.GoogleTranslator(
            source=source,
            target=target
        ).translate(separate_paragraph)

        subtitle_parts_translated.append(translated)
        
    return subtitle_parts_translated
    
### Traduz legenda:

def translate(source, target, text):
    try:
        translated = deep_translator.GoogleTranslator(
            source=source,
            target=target
        ).translate(text)
        return translated
    
    except deep_translator.exceptions.NotValidLength as err:
        print("\033[1;33mSubtitle too large detected. Translating in parts, this process takes a while. Please wait...\033[0m")
        return subtitle_parts(source, target, text)

    
### Traduz apenas um arquivo:

def translate_a_file(source, target, file, directory=""):
    if directory != "":
        file = f"subtitle/{file}"
        
    f = open(f"{file}")
    f_text = f.read()
    
    print("\033[1;33mTranslating the subtitle in parts, this process takes a little time. Please wait.\033[0m")
    print(f"\033[1;36mTranslating from \033[1;35m{source} \033[0mto \033[1;35m{target}\033[0m...\033[0m")
    
    translated = translate(source, target, f_text)
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
                 print(f"\033[1;31mThe subtitle file cannot be empty \033[35m{directory}/{file}\033[0m")
                 
    for file in files_subtitle:
        translate_a_file(source, target, file, directory="subtitle")

### Escreve um novo arquivo traduzido:

def file_write(file, translated):
    
    if type(translated) == list:
        f = open(file, 'w')
        
        for line in translated:
            f.write(line + "\n\n")
            
        f.close()
        print(f'\033[1;32mLong translation completed successfully in \033[1;35m{f.name}\033[0m')

    else:
        f = open(file, 'w')
        f.write(translated)
        f.close()
        print(f'\033[1;32mMinimal translation completed successfully in \033[1;35m{f.name}\033[0m')
    

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
    parse.set_usage('./translateAuto.py --source=<language> --target=<language> --file=<file>')
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
                    translate_a_file(options.source, options.target, options.file)
        
                else:
                    print("The subtitle file cannot be empty")
            else:
                print(".srt subtitle file is required.")
                
    elif options.source and \
         options.target and \
         options.all:
         
         if isdir("subtitle"):
            translate_all_files(options.source, options.target, directory="subtitle")
            
         else:
            exit(f"\033[1;31mThis directory does not exist: \033[1;34m{options.directory}\033[0m")
    
    elif options.languages:
        print("All languages available:")
        print(languages)

    elif options.version:
        print(f"Current version: {parse.version}")
        
    else:
        print("Try using the options -h,--help")
    
options()
