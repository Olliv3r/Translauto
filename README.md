# Translate-Auto
Traduz arquivos de legendas .srt
![main](https://github.com/Olliv3r/Translate-Auto/blob/main/media/main.gif)

### Observação
Obs:
> Traduza um ou múltiplos arquivos de legendas

### Instalação
Instalar:
```
apt update && apt install git python python-pip -y
git clone https://github.com/Olliv3r/Translate-Auto
cd Translate-Auto && pip install requirements.txt
```

### Modo de Uso:
  -v, --version         [Versão do Program]
  -s SOURCE, 
  --source=SOURCE		[Idioma de origem]
  -t TARGET, 
  --target=TARGET		[Idioma alvo]
  -f FILE, --file=FILE  [Arquivo de legenda .srt]
  -a DIRECTORY, 
  --all=DIRECTORY
                        [Traduz vários arquivos de legenda .srt de um diretório expecífico]
  -l, --languages       [Lista todos os idiomas]

### Exemplos:
Traduz a legenda de um arquivo específico:
```
./translateAuto.py -s en -t pt -f subtitle
```
Traduz a legenda de múltiplos arquivos de um diretório expecífico:
```
./translateAuto -s en -t pt -a directory_subtitle
```

### Resultado
Traduzido de:
![not-translated](https://github.com/Olliv3r/Translate-Auto/blob/main/media/not-translated.jpg)
Para:
![translated](https://github.com/Olliv3r/Translate-Auto/blob/main/media/translated.jpg)


### Nota!:
Nos exemplos acima foi feito a tradução apenas do idioma `english` para o `portuguese`, é possível traduzir o arquivo para uma variedade de idiomas que pode ser consultado usando a opção `--languages`:
```
./translateAuto.py --languages
```

© Copyright [Olliver](https://github.com/Olliv3r/).
