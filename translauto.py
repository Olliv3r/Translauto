#!/usr/bin/env python3
# Tradutor básico de legendas "srt"
#
# Por oliver, 8 de dezembro de 2023

w = '\033[0m'
r = '\033[1;31m'
g = '\033[1;32m'
y = '\033[1;33m'
b = '\033[1;34m'
c = '\033[1;35m'
m = '\033[1;36m'

from os.path import (isfile, isdir)
from os import environ, system
from subprocess import Popen, PIPE
from optparse import OptionParser
from src.language import languages
from src.menu import banner
from sys import argv, path

try:
  from deep_translator import GoogleTranslator
  from deep_translator.exceptions import (NotValidLength, TooManyRequests, RequestError, LanguageNotSupportedException)
except ModuleNotFoundError as err:
  exit(f'{w}[{y}x{w}]{w} Nenhum módulo nomeado {m}{err.name}{w}.\n{w}[{y}?{w}]{w} Execute {g}pip3 install <pacote_name>{w} para instalá-lo.\n{w}[{y}x{w}]{w} Ou execute {g}pip install -r requirements.txt{w} para instalar requisitos.')

version = '0.1.0'

### Traduz
def translate(source = 'auto', target = 'pt', text = 'translate'):
  try:
    translated = GoogleTranslator(source, target).translate(text)
    return translated
  except NotValidLength:
    print(f'{w}[{y}!{w}] Legenda muito grande detectada, traduzindo por partes. Este processo pode demorar um pouco, por favor, aguarde...{w}\n')
    return translate_parts(text, source, target)
  except LanguageNotSupportedException:
    exit(f'{w}[{r}x{w}] Idioma inválido, tente {argv[0]} -l{w}')
  except TooManyRequests:
    exit(f'{w}[{r}x{w}]{r} Ocorreu um problema de conexão{w}')
  except RequestError:
    exit(f'{w}[{r}x{w}]{r} Ocorreu um problema de conexão')
    
### Traduz legenda em partes
def translate_parts(text, source, target):
  subtitle_parts_translated = []
  subtitle_split = text.split("\n\n")
  
  for separate_paragraph in subtitle_split:
    translated = translate(source, target, separate_paragraph)
    
    subtitle_parts_translated.append(translated)
  return subtitle_parts_translated

### Traduz um arquivo
def translate_file(source, target, file, replace_file = False):
  if isfile(file):
    if file.split('.')[-1] == 'srt':
      if check_content_file(file):
        text_opened = open(file).read()
        print(f"{w}[{b}*{w}] Traduzindo de {m}{source} {w}para {m}{target}{w}...\n")
        text_translated = translate(source, target, text_opened)
        write_to_file(file, text_translated, target, replace_file)
      else:
        print(f'{w}[{r}×{w}] Arquivo vazio: {m}{file}{w}')
    else:
      print(f'{w}[{r}×{w}] Extensão inválida: {m}{file}{w}')
  else:
    if bool(file.split('/')[-1]):
      print(f'{w}[{r}×{w}] Arquivo não encontrado: {m}{file}{w}')

### Traduz mais de um arquivo
def translate_files(source, target, directory, replace_file = False):
  command = [f'ls {directory}']
  output = Popen(command, shell = True, stdout = PIPE, stderr = PIPE, text = True)
  files = output.stdout.read().split("\n")
  files_subtitle = []

  for file in files:
    files_subtitle.append(file)
    
  for file in files_subtitle:
    path_file = f"{directory}/{file}"
    translate_file(source, target, path_file, 
      replace_file = replace_file)

### Verifica conteúdo do(e) arquivo(s)
def check_content_file(file):
  file_opened = open(file)
  return file_opened.read() != ""

### Escreve arquivo(s)
def write_to_file(file, text, target, replace_file):
  file_opened = open(file ,'r')

  if replace_file:
    name_file = file_opened.name
  else:
    name_file = file_opened.name.replace('.srt', f'-{target}.srt')

  file_open = open(name_file, 'w')
  
  if type(text) == list:
    for index_text in text:
      file_open.write(f"{index_text}\n\n")
  else:
    file_open.write(text)

  file_open.close()
  print(f'{w}[{b}√{w}] Traduzido em {m}{file_open.name}{w}\n')

if __name__ == '__main__':
  parse = OptionParser()
  parse.description = "Traduz arquivos de legenda para qualquer idioma disponível"
  parse.set_usage('./translauto.py -s LANG_SRC -t LANG_DST -f FILE | -a')
  parse.add_option('-v', '--version', help = 'Versão atual do programa', action = 'store_true')
  parse.add_option('-s', '--source', dest = 'source', help = 'Idioma de origem')
  parse.add_option('-t', '--target', dest = 'target', help = 'Idioma de destino')
  parse.add_option('-f', '--file', dest= 'file', help = 'Arquivo de legenda ".srt"')
  parse.add_option('-r', '--replace-file', help = 'Substitui o(s) arquivo(s) de origem por novo(s) traduzido(s)', action = 'store_true')
  parse.add_option('-a', '--all', action = 'store_true', help = 'Traduz todos os arquivos de legenda .srt disponíveis dentro do diretório padrão')
  parse.add_option('-l', '--languages', action = 'store_true', help = 'Lista todos os idiomas')
  parse.version = version
  options, args = parse.parse_args()
  
  if options.version:
    print(parse.version)
  elif options.source:
    if options.target:
      if options.file:
        if options.replace_file:
          banner()
          translate_file(options.source, options.target, options.file, replace_file = True)
        else:
          banner()
          translate_file(options.source, options.target, options.file, replace_file = False)
          
      elif options.all:
        directory = environ.get('T_AUTO_DIR') or 'subtitle'
        if options.replace_file:
          banner()
          print(f'{w}[{b}*{w}] Traduzindo todos os arquivos de {m}{directory}{w}\n')
          translate_files(options.source, options.target, directory, replace_file = True)
        else:
          banner()
          translate_files(options.source, options.target, directory)
      else:
        print(f'{w}[{y}×{w}]{w} Faltou expecificar o arquivo ou diretório{w}.')
    else:
      print(f'{w}[{y}×{w}]{w} Faltou expecificar o target{w}.')
  elif options.languages:
    print(languages)
  else:
    banner()
    print(f'{w}[{y}×{w}]{w} Erro, tente: \033[3m{argv[0]}\033[0m -h, --help para ajuda.{w}')
