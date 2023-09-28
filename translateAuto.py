#!/bin/python3
#
# Tradutor simples de legendas de arquivos '.srt'
#
# Modo de Uso:
# $ python3 translateAuto.py -h
#
# Por oliver, 27 de setembro 2023
#

try:
    import deep_translator
except ModuleNotFoundError as err:
    exit(err)

import optparse
from src.language import languages

def subtitle_parts(source, target, text):
    match_split = '{1,2}:{1,2}:{1,2},{1,3} --> {1,2}:{1,2}:{1,2},{1,3}'
    #subtitle_parts_untranslated = []
    subtitle_parts_translated = []
    subtitle_split = text.split("\n\n")

    for separate_paragraph in subtitle_split:
        translated = deep_translator.GoogleTranslator(
            source=source,
            target=target
        ).translate(separate_paragraph)

        subtitle_parts_translated.append(translated)
        
    return subtitle_parts_translated
    
### Transl:

def transl(source, target, text):
    try:
        translated = deep_translator.GoogleTranslator(
            source=source,
            target=target
        ).translate(text)
        return translated
    
    except deep_translator.exceptions.NotValidLength as err:
        print("\033[1;33mSubtitle too large detected. Translating in parts, this process takes a while. Please wait...\033[0m")
        return subtitle_parts(source, target, text)

### Escreve tradução mínima e longa:

def file_write(file_name, translated):
    if type(translated) == list:
        f = open(file_name, 'w')
        
        for line in translated:
            f.write(line + "\n\n")
            
        f.close()
        exit(f'\033[1;32mLong translation completed successfully in ./\033[1;35m{f.name}\033[0m')
    else:
    
        f = open(file_name, 'w')
        f.write(str(translated))
        f.close()
        exit(f'\033[1;32mMinimal translation completed successfully in ./\033[1;35m{f.name}\033[0m')

### Transl_one:

def transl_one(source, target, file):
    f = open(file)
    f_text = f.read()
    
    print("\033[1;33mTranslating the subtitle in parts, this process takes a little time. Please wait.\033[0m")
    print(f"\033[1;36mTranslating from \033[1;35m{source} \033[0mto \033[1;35m{target}\033[0m...\033[0m")
    
    translated = transl(source, target, f_text)
    new_name_file = f.name.replace('.srt', f'-{target}.srt')
    file_write(new_name_file, translated)
    
### Options:

def options():
    parse = optparse.OptionParser()
    parse.add_option("-s", "--source", dest="source", help="Idioma de origem")
    parse.add_option("-t", "--target", dest="target", help="Idioma alvo")
    parse.add_option("-f", "--file", dest="file", help="Arquivo de legenda .srt")
    options, args = parse.parse_args()

    if options.source and\
         options.target and\
         options.file and options.file.split('.')[-1] == "srt":
        transl_one(options.source, options.target, options.file)

    if options.source not in languages.values() or\
        options.target  not in languages.values():
        print("Select a:")
        print(languages.values())

    if not options.file:
        print("Subtitle file is required")

    if options.file.split('.')[-1] != "srt":
        print(".srt subtitle file is required")

    else:
        exit("Tente -h")
    
options()
