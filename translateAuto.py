#!/bin/python3
#
# Tradutor simples de legendas de arquivos '.srt'
#
# Nota!: Para realizar a tradução corretamente, execute o script dentro do diretório onde se encontram os arquivos de legendas
#
# Modo de Uso:
# $ python3 translateAuto.py
#
# Por oliver, 27 de setembro 2023
#

try:
    from deep_translator import GoogleTranslator
except ModuleNotFoundError as err:
    exit(err)
import subprocess

match = "{0,9}{0,9}\n{0,9}{0,9}:{0,9}{0,9}:{0,9}{0,9},{0,9}{0,9}{0,9} --> {0,9}{0,9}:{0,9}{0,9}:{0,9}{0,9},{0,9}{0,9}{0,9}\n[-a-z.]"

files = []
output = subprocess.Popen(["ls"], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

result = output.stdout.read().split("\n")
list_untranslated_paragraphs = []
list_translated_paragraphs = []

### Seperate_output
def seperate_output():
    for res in result:
        if ".srt" in res:
            file = res.replace("\\","")
            files.append(file)

    return files
    
### Transl (Pode Alterar o 'source' e 'target')
def transl(text):

    translated = GoogleTranslator(
        source='english',
        target='portuguese'
    ).translate(text)

    return translated

### Transl_all
def transl_all():
    files = seperate_output()

    if len(files) == 0:
        exit("\033[1;31mNo nobtitle file found!\033[0m")

    print("\033[1;33mTranslating the subtitle in parts, this process takes a little time. Please wait.\033[0m")
    print(f"\033[1;34mTotal subtitle file to be translated: \033[1;35m{len(files)}\033[0m")

    for file in files:
        open_file = open(file)
        paragraphs_together = open_file.read().split(match)
    
        for paragraph_together in paragraphs_together:
            separate_paragraphs = paragraph_together.split("\n\n")

        for separate_paragraph in separate_paragraphs:
            list_untranslated_paragraphs.append({f'{open_file.name}': separate_paragraph})

        
        for dictt in list_untranslated_paragraphs:
            new_name_file = file.replace(".srt", "-portuguese.srt")
            new_file = open(new_name_file, 'w')

            for paragraph_not_translated in dictt.values():
                translated_paragraph = transl(paragraph_not_translated)
                list_translated_paragraphs.append({f'{open_file.name}': translated_paragraph})

                
            for dictt in list_translated_paragraphs:
                for value in dictt.values():
                    new_file.write(f"{value}\n\n")
                    
        new_file.close()
        print(f'\033[1;32mTranslate successfully in ./\033[1;35m{new_file.name}\033[0m')


transl_all()
