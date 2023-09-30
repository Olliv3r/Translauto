# Translate-Auto
Traduz arquivos de legenda .srt
![main](https://github.com/Olliv3r/Translate-Auto/blob/main/media/main.gif)

### Instalação
Instalar:
```
apt update && apt install git python python-pip -y
git clone https://github.com/Olliv3r/Translate-Auto
cd Translate-Auto && pip install -r requirements.txt
```

### Modo de Uso:
  -v, --version         Versão do Program
  -s SOURCE, 
  --source=SOURCE		    Idioma de origem
  -t TARGET, 
  --target=TARGET		    Idioma alvo
  -f FILE, --file=FILE  Arquivo de legenda .srt
  -a DIRECTORY, 
  --all=DIRECTORY
                        Traduz vários arquivos de legenda .srt de um diretório expecífico
  -l, --languages       Lista todos os idiomas

### Exemplos:
Traduz a legenda de um arquivo específico:
```
./translateAuto.py -s en -t pt -f subtitle/subtitle.srt
```
Traduz a legenda de múltiplos arquivos do diretório padrão `subtitle`:
```
./translateAuto -s en -t pt -a directory_subtitle
```

### Obs:
Caso queira traduzir vários arquivos de legenda `.srt` você precisa copiá-los para dentro do diretório `subtitle` o qual o programa usa para traduzir mais de um arquivo de legenda `.srt`. Se for apenas um arquivo não há necessidade de fazer esta etapa.

### Nota:
Nos exemplos acima a tradução foi realizada somente do idioma `english` para o `portuguese`, é possível traduzir o arquivo para qualquer idioma disponível. Todos os idiomas podem ser acessados usando a opção `--languages`:
```
./translateAuto.py --languages
```

### Recurso:
[-] Tradução de arquivos de legendas
[ ] Outros

© Copyright [Olliver](https://github.com/Olliv3r/).
